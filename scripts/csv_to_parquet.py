#!/usr/bin/env python3
"""
Converte CSV para Parquet em streaming (sem carregar o ficheiro inteiro na RAM).

Adequado a ficheiros muito grandes (ex.: Indian Weather). Requer: pip install -r requirements.txt

Documentação: scripts/csv_to_parquet.md (na mesma pasta que este .py).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pyarrow as pa
import pyarrow.csv as pacsv
import pyarrow.parquet as pq


def convert_csv_to_parquet(
    src: Path,
    dst: Path,
    *,
    compression: str = "zstd",
    read_block_bytes: int = 8 * 1024 * 1024,
) -> None:
    src = src.resolve()
    dst = dst.resolve()
    if not src.is_file():
        raise FileNotFoundError(f"Input not found: {src}")

    dst.parent.mkdir(parents=True, exist_ok=True)

    read_options = pacsv.ReadOptions(block_size=read_block_bytes)
    reader = pacsv.open_csv(str(src), read_options=read_options)

    writer: pq.ParquetWriter | None = None
    rows = 0
    try:
        while True:
            try:
                batch = reader.read_next_batch()
            except StopIteration:
                break
            if batch.num_rows == 0:
                break
            table = pa.Table.from_batches([batch])
            rows += table.num_rows
            if writer is None:
                writer = pq.ParquetWriter(
                    str(dst),
                    table.schema,
                    compression=compression,
                )
            writer.write_table(table)
    finally:
        if writer is not None:
            writer.close()

    print(f"Wrote {rows:,} rows to {dst}", file=sys.stderr)


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    default_in = repo / "data" / "archive" / "Indian_Weather_Dataset.csv"
    default_out = repo / "data" / "archive" / "Indian_Weather_Dataset.parquet"

    p = argparse.ArgumentParser(description="Stream CSV to Parquet (low memory).")
    p.add_argument(
        "-i",
        "--input",
        type=Path,
        default=default_in,
        help=f"Input CSV (default: {default_in})",
    )
    p.add_argument(
        "-o",
        "--output",
        type=Path,
        default=default_out,
        help=f"Output Parquet (default: {default_out})",
    )
    p.add_argument(
        "--compression",
        default="zstd",
        choices=("snappy", "zstd", "gzip", "lz4", "brotli"),
        help="Parquet codec (default: zstd).",
    )
    p.add_argument(
        "--read-block-mib",
        type=int,
        default=8,
        metavar="N",
        help="CSV parser block size in MiB (default: 8).",
    )
    args = p.parse_args()

    try:
        convert_csv_to_parquet(
            args.input,
            args.output,
            compression=args.compression,
            read_block_bytes=max(1, args.read_block_mib) * 1024 * 1024,
        )
    except FileNotFoundError as e:
        print(e, file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
