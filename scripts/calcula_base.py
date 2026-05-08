from pathlib import Path

import numpy as np
import pyarrow.parquet as pq
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, coalesce, lit


TARGET_COL = "temperature_C"
HOUR_COL = "hour"
MONTH_COL = "month"
SEED = 42
TRAIN_RATIO = 0.7
PARQUET_PATH = Path(__file__).resolve().parents[1] / "data" / "Indian_Weather_Dataset.parquet"


def calc_metrics(y_true: np.ndarray, y_pred: np.ndarray) -> dict[str, float]:
    err = y_true - y_pred
    mae = float(np.mean(np.abs(err)))
    rmse = float(np.sqrt(np.mean(err**2)))
    denom = float(np.sum((y_true - np.mean(y_true)) ** 2))
    r2 = float(1.0 - (np.sum(err**2) / denom)) if denom > 0 else 0.0
    return {"mae": mae, "rmse": rmse, "r2": r2}


def print_metrics(metrics: dict[str, float]) -> None:
    print(f"MAE : {metrics['mae']:.4f}")
    print(f"RMSE: {metrics['rmse']:.4f}")
    print(f"R2  : {metrics['r2']:.4f}")
    print("-----------------------------------\n")


def print_comparison(results: list[tuple[str, dict[str, float]]]) -> None:
    print("Comparativo de baselines")
    print(f"{'Modelo':<24} {'MAE':>10} {'RMSE':>10} {'R2':>10}")
    print("-" * 58)
    for name, m in results:
        print(f"{name:<24} {m['mae']:>10.4f} {m['rmse']:>10.4f} {m['r2']:>10.4f}")
    print("-" * 58 + "\n")


def run_with_spark() -> None:
    spark = SparkSession.builder.appName("T030_Baseline_Root").master("local[*]").getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    try:
        df = spark.read.parquet(str(PARQUET_PATH)).select(TARGET_COL, HOUR_COL, MONTH_COL)
        train_data, test_data = df.randomSplit([TRAIN_RATIO, 1.0 - TRAIN_RATIO], seed=SEED)
        train_data = train_data.filter(col(TARGET_COL).isNotNull())
        test_data = test_data.filter(col(TARGET_COL).isNotNull())

        print("Baselines de regressao [Spark]")
        print(f"Linhas treino: {train_data.count()}")
        print(f"Linhas teste : {test_data.count()}")

        global_mean = float(train_data.select(avg(col(TARGET_COL)).alias("avg_target")).first()["avg_target"])
        print(f"Media global no treino: {global_mean:.4f}\n")

        def eval_df(pred_df):
            mae = RegressionEvaluator(labelCol=TARGET_COL, predictionCol="prediction", metricName="mae").evaluate(pred_df)
            rmse = RegressionEvaluator(labelCol=TARGET_COL, predictionCol="prediction", metricName="rmse").evaluate(pred_df)
            r2 = RegressionEvaluator(labelCol=TARGET_COL, predictionCol="prediction", metricName="r2").evaluate(pred_df)
            return {"mae": float(mae), "rmse": float(rmse), "r2": float(r2)}

        results = []

        pred_const = test_data.withColumn("prediction", lit(global_mean))
        results.append(("media_global", eval_df(pred_const)))

        mean_by_hour = train_data.groupBy(HOUR_COL).agg(avg(TARGET_COL).alias("pred_hour"))
        pred_hour = (
            test_data.join(mean_by_hour, on=HOUR_COL, how="left")
            .withColumn("prediction", coalesce(col("pred_hour"), lit(global_mean)))
            .drop("pred_hour")
        )
        results.append(("media_por_hour", eval_df(pred_hour)))

        mean_by_month = train_data.groupBy(MONTH_COL).agg(avg(TARGET_COL).alias("pred_month"))
        pred_month = (
            test_data.join(mean_by_month, on=MONTH_COL, how="left")
            .withColumn("prediction", coalesce(col("pred_month"), lit(global_mean)))
            .drop("pred_month")
        )
        results.append(("media_por_month", eval_df(pred_month)))

        mean_by_hour_month = train_data.groupBy(HOUR_COL, MONTH_COL).agg(avg(TARGET_COL).alias("pred_hm"))
        pred_hm = (
            test_data.join(mean_by_hour_month, on=[HOUR_COL, MONTH_COL], how="left")
            .withColumn("prediction", coalesce(col("pred_hm"), lit(global_mean)))
            .drop("pred_hm")
        )
        results.append(("media_por_hour_month", eval_df(pred_hm)))

        print_comparison(results)
    finally:
        spark.stop()


def run_with_pyarrow_fallback() -> None:
    print("Baselines de regressao [PyArrow fallback]")
    table = pq.read_table(PARQUET_PATH, columns=[TARGET_COL, HOUR_COL, MONTH_COL])
    y = table.column(TARGET_COL).to_numpy(zero_copy_only=False).astype("float64", copy=False)
    h = table.column(HOUR_COL).to_numpy(zero_copy_only=False).astype("float64", copy=False)
    m = table.column(MONTH_COL).to_numpy(zero_copy_only=False).astype("float64", copy=False)

    valid_y = ~np.isnan(y)
    y = y[valid_y]
    h = h[valid_y]
    m = m[valid_y]

    if y.size == 0:
        raise ValueError("Sem valores validos para temperature_C.")

    rng = np.random.default_rng(SEED)
    idx = np.arange(y.size)
    rng.shuffle(idx)
    split = int(TRAIN_RATIO * y.size)
    train_idx, test_idx = idx[:split], idx[split:]
    y_train, y_test = y[train_idx], y[test_idx]
    h_train, h_test = h[train_idx], h[test_idx]
    m_train, m_test = m[train_idx], m[test_idx]

    global_mean = float(np.mean(y_train))

    hour_means = {}
    for hour in np.unique(h_train[~np.isnan(h_train)]):
        mask = h_train == hour
        hour_means[int(hour)] = float(np.mean(y_train[mask]))

    month_means = {}
    for month in np.unique(m_train[~np.isnan(m_train)]):
        mask = m_train == month
        month_means[int(month)] = float(np.mean(y_train[mask]))

    hm_means = {}
    hm_pairs = np.column_stack((h_train, m_train))
    hm_valid = ~np.isnan(hm_pairs).any(axis=1)
    hm_pairs = hm_pairs[hm_valid].astype(np.int64, copy=False)
    y_hm = y_train[hm_valid]
    unique_pairs = np.unique(hm_pairs, axis=0)
    for hour, month in unique_pairs:
        mask = (hm_pairs[:, 0] == hour) & (hm_pairs[:, 1] == month)
        hm_means[(int(hour), int(month))] = float(np.mean(y_hm[mask]))

    print(f"Linhas treino: {y_train.size}")
    print(f"Linhas teste : {y_test.size}")
    print(f"Media global no treino: {global_mean:.4f}\n")

    pred_const = np.full_like(y_test, fill_value=global_mean, dtype=np.float64)

    pred_hour = np.full_like(y_test, fill_value=global_mean, dtype=np.float64)
    for i in range(y_test.size):
        if not np.isnan(h_test[i]):
            pred_hour[i] = hour_means.get(int(h_test[i]), global_mean)

    pred_month = np.full_like(y_test, fill_value=global_mean, dtype=np.float64)
    for i in range(y_test.size):
        if not np.isnan(m_test[i]):
            pred_month[i] = month_means.get(int(m_test[i]), global_mean)

    pred_hm = np.full_like(y_test, fill_value=global_mean, dtype=np.float64)
    for i in range(y_test.size):
        if not np.isnan(h_test[i]) and not np.isnan(m_test[i]):
            pred_hm[i] = hm_means.get((int(h_test[i]), int(m_test[i])), global_mean)

    results = [
        ("media_global", calc_metrics(y_test, pred_const)),
        ("media_por_hour", calc_metrics(y_test, pred_hour)),
        ("media_por_month", calc_metrics(y_test, pred_month)),
        ("media_por_hour_month", calc_metrics(y_test, pred_hm)),
    ]
    print_comparison(results)


if __name__ == "__main__":
    if not PARQUET_PATH.exists():
        raise FileNotFoundError(f"Parquet nao encontrado em: {PARQUET_PATH}")

    try:
        run_with_spark()
    except Exception as exc:
        if "getSubject is not supported" not in str(exc):
            raise
        print("Spark falhou com 'getSubject is not supported'.")
        print("Executando fallback local com PyArrow para concluir o baseline.\n")
        run_with_pyarrow_fallback()