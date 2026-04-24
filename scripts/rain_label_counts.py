#!/usr/bin/env python3
"""
Conta frequências da coluna alvo (por defeito `rain_label`) num Parquet, só com PyArrow.
Saída em Markdown para colar em docs/imbalance.md (T023).

Documentação: scripts/rain_label_counts.md
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    default_in = repo / "data" / "Indian_Weather_Dataset.parquet"

    p = argparse.ArgumentParser(
        description="Frequências da coluna alvo no Parquet (Markdown no stdout)."
    )
    p.add_argument(
        "-i",
        "--input",
        type=Path,
        default=default_in,
        help=f"Parquet (por defeito: {default_in})",
    )
    p.add_argument(
        "--column",
        type=str,
        default="rain_label",
        help="Nome da coluna (por defeito: rain_label)",
    )
    args = p.parse_args()

    src = args.input.resolve()
    if not src.is_file():
        print(f"ERRO: ficheiro não encontrado: {src}", file=sys.stderr)
        return 1

    try:
        tbl = pq.read_table(src, columns=[args.column])
    except Exception as e:
        print(f"ERRO ao ler coluna {args.column!r}: {e}", file=sys.stderr)
        return 1

    arr = tbl.column(0).combine_chunks()
    n = len(arr)
    if n == 0:
        print("ERRO: coluna vazia.", file=sys.stderr)
        return 1

    vc = pc.value_counts(arr)
    vals = vc.field(0)
    cnts = vc.field(1)
    pairs = list(zip(vals.to_pylist(), cnts.to_pylist()))
    pairs.sort(key=lambda x: (-x[1], str(x[0])))

    total = sum(c for _, c in pairs)
    print(f"### Frequências de `{args.column}` (`{src}`)\n")
    print("| classe | contagem | % do total |")
    print("|--------|----------|------------|")
    for val, cnt in pairs:
        label = "NULL" if val is None else str(val)
        pct = 100.0 * cnt / total if total else 0.0
        print(f"| {label} | {cnt:,} | {pct:.4f} |")
    print(f"\n**Total (soma das classes na contagem):** {total:,}  ")
    print(f"**Linhas lidas na coluna:** {n:,}")
    if arr.null_count:
        print(f"**Nulos na coluna (fora do value_counts):** {arr.null_count:,}")
    print(f"\n**pyarrow:** {pa.__version__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
