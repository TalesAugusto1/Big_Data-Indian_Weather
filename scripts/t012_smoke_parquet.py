#!/usr/bin/env python3
"""
Smoke T012: ler Parquet no contentor Spark (bind mount em /dataset).

Variáveis de ambiente:
  T012_PARQUET_PATH  Caminho dentro do contentor (por defeito: /dataset/Indian_Weather_Dataset.parquet)
  T012_FULL_COUNT    Definir como "1" para executar df.count() (varredura completa — lenta em ficheiros enormes)
"""
from __future__ import annotations

import os
import sys


def main() -> int:
    default_path = "/dataset/Indian_Weather_Dataset.parquet"
    path = os.environ.get("T012_PARQUET_PATH", default_path).strip()

    if not os.path.exists(path):
        print(
            f"ERRO: Parquet não encontrado em {path!r}.\n"
            "Monte ./data do repositório em /dataset (ver docker-compose.yml) e confirme que o ficheiro existe, p.ex.:\n"
            "  data/Indian_Weather_Dataset.parquet\n"
            "  ou defina T012_PARQUET_PATH=/dataset/archive/Indian_Weather_Dataset.parquet",
            file=sys.stderr,
        )
        return 1

    try:
        from pyspark.sql import SparkSession  # type: ignore[import-untyped]
    except ImportError as e:
        print(f"ERRO: PySpark indisponível: {e}", file=sys.stderr)
        return 1

    spark = (
        SparkSession.builder.appName("T012_smoke_parquet")
        .master("local[1]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    try:
        df = spark.read.parquet(path)
        print("=== Esquema ===")
        df.printSchema()
        print("=== Amostra (1 linha) ===")
        df.show(1, vertical=False, truncate=80)
        n = df.limit(1).count()
        print(f"=== limit(1).count() === {n}")
        if os.environ.get("T012_FULL_COUNT") == "1":
            total = df.count()
            print(f"=== count() completo === {total}")
    finally:
        spark.stop()

    print("Smoke T012: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
