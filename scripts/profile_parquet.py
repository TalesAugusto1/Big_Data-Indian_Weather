#!/usr/bin/env python3
"""
Perfil agregado de um Parquet (PyArrow apenas): nulos, tipos, min/max numéricos,
contagem aproximada de distintos em strings (amostra opcional).

Serve para fundamentar missing/cardinalidade na documentação (T022 / T024)
sem usar pandas nem scikit-learn.

Documentação: scripts/profile_parquet.md
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq


def _pct(part: int, whole: int) -> str:
    if whole <= 0:
        return "N/A"
    return f"{100.0 * part / whole:.4f}"


def _min_max_str(arr: pa.ChunkedArray | pa.Array) -> tuple[str, str]:
    if len(arr) == 0:
        return "N/A", "N/A"
    mm = pc.min_max(arr)
    if mm.is_valid:
        d = mm.as_py()
        return str(d["min"]), str(d["max"])
    return "N/A", "N/A"


def _distinct_count(arr: pa.Array | pa.ChunkedArray, sample_rows: int | None) -> tuple[int, str]:
    """
    Returns (count, nota). If sample_rows is set and len(arr) > sample_rows,
    distinct is computed only on arr[:sample_rows].
    """
    combined = arr if isinstance(arr, pa.Array) else arr.combine_chunks()
    n = len(combined)
    note = ""
    if sample_rows is not None and n > sample_rows:
        combined = combined.slice(0, sample_rows)
        note = f" (distintos só nas primeiras {sample_rows:,} linhas)"
        n = len(combined)
    if n == 0:
        return 0, note
    try:
        c = pc.count_distinct(combined, mode="all")
        val = int(c.as_py()) if c.is_valid else 0
    except Exception:
        # fallback: unique + len (pode ser pesado)
        try:
            u = pc.unique(combined)
            val = len(u) if u is not None else 0
        except Exception:
            val = -1
            note += " (distinct indisponível)"
    return val, note


def profile_column(
    path: Path,
    name: str,
    *,
    sample_rows: int | None,
) -> dict[str, str]:
    tbl = pq.read_table(path, columns=[name])
    arr = tbl.column(0).combine_chunks()
    n = len(arr)
    nulls = arr.null_count
    dtype = str(arr.type)

    distinct_s = "N/A"
    if pa.types.is_integer(arr.type) or pa.types.is_floating(arr.type) or pa.types.is_decimal(
        arr.type
    ):
        d, note = _distinct_count(arr, sample_rows)
        distinct_s = f"{d:,}{note}"
    elif pa.types.is_boolean(arr.type):
        d, note = _distinct_count(arr, sample_rows)
        distinct_s = f"{d:,}{note}"
    elif pa.types.is_timestamp(arr.type) or pa.types.is_date(arr.type):
        d, note = _distinct_count(arr, sample_rows)
        distinct_s = f"{d:,}{note}"
    elif pa.types.is_string(arr.type) or pa.types.is_large_string(arr.type) or pa.types.is_binary(
        arr.type
    ):
        d, note = _distinct_count(arr, sample_rows)
        distinct_s = f"{d:,}{note}"
    else:
        distinct_s = "—"

    mn, mx = "N/A", "N/A"
    if (
        pa.types.is_integer(arr.type)
        or pa.types.is_floating(arr.type)
        or pa.types.is_decimal(arr.type)
        or pa.types.is_timestamp(arr.type)
        or pa.types.is_date(arr.type)
    ):
        mn, mx = _min_max_str(arr)

    return {
        "coluna": name,
        "tipo": dtype,
        "linhas": f"{n:,}",
        "nulos": f"{nulls:,}",
        "pct_nulos": _pct(nulls, n),
        "distintos": distinct_s,
        "min": mn,
        "max": mx,
    }


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    default_in = repo / "data" / "Indian_Weather_Dataset.parquet"

    p = argparse.ArgumentParser(
        description="Perfil agregado de Parquet (PyArrow): nulos, tipos, min/max, distintos."
    )
    p.add_argument(
        "-i",
        "--input",
        type=Path,
        default=default_in,
        help=f"Parquet (por defeito: {default_in})",
    )
    p.add_argument(
        "--columns",
        type=str,
        default="",
        help="Lista separada por vírgulas (opcional). Vazio = todas as colunas do ficheiro.",
    )
    p.add_argument(
        "--distinct-sample-rows",
        type=int,
        default=1_000_000,
        metavar="N",
        help="Para contagem de distintos: no máximo N linhas por coluna (por defeito 1_000_000). Use 0 para tentar o ficheiro inteiro (pode ser lento).",
    )
    args = p.parse_args()

    src = args.input.resolve()
    if not src.is_file():
        print(f"ERRO: ficheiro não encontrado: {src}", file=sys.stderr)
        return 1

    try:
        pf = pq.ParquetFile(src)
    except Exception as e:
        print(f"ERRO ao abrir Parquet: {e}", file=sys.stderr)
        return 1

    schema = pf.schema_arrow
    all_names = schema.names
    if args.columns.strip():
        wanted = {c.strip() for c in args.columns.split(",") if c.strip()}
        names = [n for n in all_names if n in wanted]
        missing = wanted - set(names)
        if missing:
            print(f"AVISO: colunas pedidas mas não encontradas: {sorted(missing)}", file=sys.stderr)
    else:
        names = list(all_names)

    if not names:
        print("ERRO: sem colunas a perfilar.", file=sys.stderr)
        return 1

    sample = None if args.distinct_sample_rows == 0 else args.distinct_sample_rows

    print("## Perfil do Parquet (PyArrow)\n")
    print(f"**Ficheiro:** `{src}`")
    print(f"**Colunas:** {len(names)}")
    if sample:
        print(f"**Amostra para distintos:** primeiras {sample:,} linhas por coluna (use `--distinct-sample-rows 0` para tentar o total).")
    else:
        print("**Amostra para distintos:** desligada (contagem no conjunto completo por coluna — pode demorar).")
    print()

    print("| coluna | tipo | linhas | nulos | % nulos | distintos | min | max |")
    print("|--------|------|--------|-------|---------|-----------|-----|-----|")
    rows: list[dict[str, str]] = []
    for name in names:
        try:
            row = profile_column(src, name, sample_rows=sample)
            rows.append(row)
        except Exception as e:
            rows.append(
                {
                    "coluna": name,
                    "tipo": "ERRO",
                    "linhas": "—",
                    "nulos": "—",
                    "pct_nulos": "—",
                    "distintos": str(e),
                    "min": "—",
                    "max": "—",
                }
            )
        r = rows[-1]
        print(
            f"| {r['coluna']} | {r['tipo']} | {r['linhas']} | {r['nulos']} | {r['pct_nulos']} | "
            f"{r['distintos']} | {r['min']} | {r['max']} |"
        )

    print()
    print("**Versão pyarrow:**", pa.__version__)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
