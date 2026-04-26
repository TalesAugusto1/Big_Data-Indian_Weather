from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("T030_Baseline_Root").getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

df = spark.read.parquet("/dataset/Indian_Weather_Dataset.parquet")

target_col = "rain_label"
train_data, test_data = df.randomSplit([0.7, 0.3], seed=42)

#Treino
print("Treino")
classe_counts = train_data.groupBy(target_col).count().orderBy(col("count").desc())
classe_counts.show()
majority_class = classe_counts.first()[target_col]
print(f"Classe Majoritária: {majority_class}\n")

test_counts = test_data.groupBy(target_col).count().collect()
test_dict = {row[target_col]: row['count'] for row in test_counts}

TP = test_dict.get(majority_class, 0)
total_test_rows = test_data.count()
FP = total_test_rows - TP
precision = TP / (TP + FP) if (TP + FP) > 0 else 0
recall = TP / TP if TP > 0 else 0
if (precision + recall) == 0:
    f1_score = 0
else:
    f1_score = 2 * (precision * recall) / (precision + recall)

print(f"F1-Score: {f1_score:.4f}")
print("-----------------------------------\n")

spark.stop()