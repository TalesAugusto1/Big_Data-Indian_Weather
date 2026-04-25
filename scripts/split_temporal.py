#!/usr/bin/env python3
"""
Split temporal reprodutível (T021): ordena por `datetime` e parte treino/val/teste por frações.

O critério principal é temporal (sem shuffle global). A seed fixa apenas o ambiente;
não há amostragem aleatória neste script.

Documentação: scripts/split_temporal.md
"""
from __future__ import annotations

import argparse
import random
import sys
from pathlib import Path

import pyarrow as pa
import pyarrow.compute as pc
import pyarrow.parquet as pq


def _split_sizes(n: int, train: float, val: float, test: float) -> tuple[int, int, int]:
    if abs(train + val + test - 1.0) > 1e-9:
        raise ValueError(f"As frações devem somar 1.0 (obtido: {train + val + test})")
    n_train = int(n * train)
    n_val = int(n * val)
    n_test = n - n_train - n_val
    if n_test < 0:
        raise ValueError("Frações inválidas: contagens negativas após arredondamento.")
    return n_train, n_val, n_test


def _format_scalar(value: pa.Scalar | None) -> str:
    if value is None or not value.is_valid:
        return "N/A"
    return str(value.as_py())


def main() -> int:
    repo = Path(__file__).resolve().parents[1]
    default_in = repo / "data" / "Indian_Weather_Dataset.parquet"

    p = argparse.ArgumentParser(
        description="Split temporal por datetime (coluna única lida do Parquet)."
    )
    p.add_argument(
        "-i",
        "--input",
        type=Path,
        default=default_in,
        help=f"Parquet de entrada (por defeito: {default_in})",
    )
    p.add_argument(
        "--train",
        type=float,
        default=0.70,
        metavar="F",
        help="Fração treino (por defeito: 0.70)",
    )
    p.add_argument(
        "--val",
        type=float,
        default=0.15,
        metavar="F",
        help="Fração validação (por defeito: 0.15)",
    )
    p.add_argument(
        "--test",
        type=float,
        default=0.15,
        metavar="F",
        help="Fração teste (por defeito: 0.15)",
    )
    p.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Seed para random/numpy (reprodutibilidade do ambiente; split é temporal).",
    )
    args = p.parse_args()

    random.seed(args.seed)

    src = args.input.resolve()
    if not src.is_file():
        print(f"ERRO: ficheiro não encontrado: {src}", file=sys.stderr)
        return 1

    try:
        table = pq.read_table(src, columns=["datetime"])
    except Exception as e:
        print(f"ERRO ao ler Parquet: {e}", file=sys.stderr)
        return 1

    if table.num_rows == 0:
        print("ERRO: dataset vazio.", file=sys.stderr)
        return 1

    if "datetime" not in table.column_names:
        print("ERRO: coluna 'datetime' não encontrada no Parquet.", file=sys.stderr)
        return 1

    dt = table.column("datetime").combine_chunks()
    dt_type = dt.type
    if not pa.types.is_timestamp(dt_type):
        # Tenta converter strings/inteiros para timestamp de forma explícita.
        try:
            dt = pc.cast(dt, pa.timestamp("us"), safe=False)
        except Exception as e:
            print(f"ERRO: não foi possível converter 'datetime' para timestamp: {e}", file=sys.stderr)
            return 1

    order = pc.sort_indices(dt)
    dt_sorted = pc.take(dt, order)

    n = len(dt_sorted)
    n_train, n_val, n_test = _split_sizes(n, args.train, args.val, args.test)

    i0 = 0
    i1 = n_train
    i2 = i1 + n_val

    parts = [
        ("treino", dt_sorted.slice(i0, n_train)),
        ("validacao", dt_sorted.slice(i1, n_val)),
        ("teste", dt_sorted.slice(i2, n_test)),
    ]

    print("## Split temporal (T021)\n")
    print("| split | linhas | min(datetime) | max(datetime) |")
    print("|-------|--------|-----------------|---------------|")
    for name, part in parts:
        if len(part) == 0:
            mn = mx = "N/A"
        else:
            mm = pc.min_max(part)
            mmv = mm.as_py() if mm.is_valid else None
            mn = str(mmv["min"]) if mmv else "N/A"
            mx = str(mmv["max"]) if mmv else "N/A"
        print(f"| {name} | {len(part):,} | {mn} | {mx} |")

    print(f"\n**Total linhas:** {n:,}")
    print(
        f"**Frações pedidas:** treino={args.train}, val={args.val}, teste={args.test} "
        f"(soma={args.train + args.val + args.test:.6f})"
    )
    print(f"**Seed:** {args.seed} (sem amostragem aleatória; ordenação estável por `datetime`)")
    print(f"**Ficheiro:** `{src}`\n")

    print("### Checagem temporal (fronteiras)\n")
    train_part = parts[0][1]
    val_part = parts[1][1]
    test_part = parts[2][1]

    train_mm = pc.min_max(train_part).as_py() if len(train_part) > 0 else None
    val_mm = pc.min_max(val_part).as_py() if len(val_part) > 0 else None
    test_mm = pc.min_max(test_part).as_py() if len(test_part) > 0 else None

    train_max = train_mm["max"] if train_mm else None
    val_min = val_mm["min"] if val_mm else None
    val_max = val_mm["max"] if val_mm else None
    test_min = test_mm["min"] if test_mm else None

    if len(val_part) > 0 and train_max is not None and val_min is not None:
        ok_tv = train_max <= val_min
        print(
            f"- max(treino) <= min(validacao): **{ok_tv}** "
            f"(treino_max={_format_scalar(pa.scalar(train_max))}, val_min={_format_scalar(pa.scalar(val_min))})"
        )
    else:
        print("- validacao vazia: ignorar checagem treino/val.")

    if len(val_part) > 0 and len(test_part) > 0 and val_max is not None and test_min is not None:
        ok_vte = val_max <= test_min
        print(
            f"- max(validacao) <= min(teste): **{ok_vte}** "
            f"(val_max={_format_scalar(pa.scalar(val_max))}, test_min={_format_scalar(pa.scalar(test_min))})"
        )
    elif len(test_part) == 0:
        print("- teste vazio: ignorar checagem val/teste.")

    print("\n### Riscos de data leakage (evitar nas fases seguintes)\n")
    bullets = [
        "Normalização ou imputação com **estatísticas globais** calculadas com treino+val+teste.",
        "Features com **janela temporal** que incluam linhas de validação/teste ao treinar.",
        "Agregações por **estado/cidade** que misturem períodos futuros e passados sem respeitar o split.",
        "**Duplicados** de `datetime` na fronteira: linhas com o mesmo timestamp podem cair em splits diferentes; avaliar agrupamento ou desempate por chave geográfica se necessário.",
        "Modelos que usam **hierarquia geo** sem split por grupo (fuga de informação entre regiões correlacionadas).",
    ]
    for b in bullets:
        print(f"- {b}")

    print("\n**Versões (registar na evidência):**")
    print(f"- pyarrow {pa.__version__}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
