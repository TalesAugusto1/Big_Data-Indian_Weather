#!/usr/bin/env python3
"""
T012 smoke test: read Parquet inside Spark container (bind mount /dataset).

Env:
  T012_PARQUET_PATH  Path inside container (default: /dataset/Indian_Weather_Dataset.parquet)
  T012_FULL_COUNT    Set to "1" to run df.count() (full scan — slow on huge files)
"""
from __future__ import annotations

import os
import sys


def main() -> int:
    default_path = "/dataset/Indian_Weather_Dataset.parquet"
    path = os.environ.get("T012_PARQUET_PATH", default_path).strip()

    if not os.path.exists(path):
        print(
            f"ERROR: Parquet not found at {path!r}.\n"
            "Mount repo ./data to /dataset (see docker-compose.yml) and ensure the file exists, e.g.:\n"
            "  data/Indian_Weather_Dataset.parquet\n"
            "  or set T012_PARQUET_PATH=/dataset/archive/Indian_Weather_Dataset.parquet",
            file=sys.stderr,
        )
        return 1

    try:
        from pyspark.sql import SparkSession  # type: ignore[import-untyped]
    except ImportError as e:
        print(f"ERROR: PySpark not available: {e}", file=sys.stderr)
        return 1

    spark = (
        SparkSession.builder.appName("T012_smoke_parquet")
        .master("local[1]")
        .getOrCreate()
    )
    spark.sparkContext.setLogLevel("WARN")

    try:
        df = spark.read.parquet(path)
        print("=== Schema ===")
        df.printSchema()
        print("=== Sample (1 row) ===")
        df.show(1, vertical=False, truncate=80)
        n = df.limit(1).count()
        print(f"=== limit(1).count() === {n}")
        if os.environ.get("T012_FULL_COUNT") == "1":
            total = df.count()
            print(f"=== FULL count() === {total}")
    finally:
        spark.stop()

    print("T012 smoke: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
