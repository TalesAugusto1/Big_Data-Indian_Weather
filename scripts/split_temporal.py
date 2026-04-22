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

import pandas as pd


def _split_sizes(n: int, train: float, val: float, test: float) -> tuple[int, int, int]:
    if abs(train + val + test - 1.0) > 1e-9:
        raise ValueError(f"As frações devem somar 1.0 (obtido: {train + val + test})")
    n_train = int(n * train)
    n_val = int(n * val)
    n_test = n - n_train - n_val
    if n_test < 0:
        raise ValueError("Frações inválidas: contagens negativas após arredondamento.")
    return n_train, n_val, n_test


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
        df = pd.read_parquet(src, columns=["datetime"], engine="pyarrow")
    except Exception as e:
        print(f"ERRO ao ler Parquet: {e}", file=sys.stderr)
        return 1

    if df.empty:
        print("ERRO: dataset vazio.", file=sys.stderr)
        return 1

    df["datetime"] = pd.to_datetime(df["datetime"], utc=False)
    df = df.sort_values("datetime", kind="mergesort").reset_index(drop=True)

    n = len(df)
    n_train, n_val, n_test = _split_sizes(n, args.train, args.val, args.test)

    i0 = 0
    i1 = n_train
    i2 = i1 + n_val

    parts = [
        ("treino", df.iloc[i0:i1]),
        ("validacao", df.iloc[i1:i2]),
        ("teste", df.iloc[i2:]),
    ]

    print("## Split temporal (T021)\n")
    print("| split | linhas | min(datetime) | max(datetime) |")
    print("|-------|--------|-----------------|---------------|")
    for name, part in parts:
        mn = part["datetime"].min()
        mx = part["datetime"].max()
        print(f"| {name} | {len(part):,} | {mn} | {mx} |")

    print(f"\n**Total linhas:** {n:,}")
    print(
        f"**Frações pedidas:** treino={args.train}, val={args.val}, teste={args.test} "
        f"(soma={args.train + args.val + args.test:.6f})"
    )
    print(f"**Seed:** {args.seed} (sem amostragem aleatória; ordenação mergesort por `datetime`)")
    print(f"**Ficheiro:** `{src}`\n")

    print("### Checagem temporal (fronteiras)\n")
    train_max = parts[0][1]["datetime"].max()
    val_min = parts[1][1]["datetime"].min()
    val_max = parts[1][1]["datetime"].max()
    test_min = parts[2][1]["datetime"].min()
    if len(parts[1][1]) > 0:
        ok_tv = train_max <= val_min
        print(f"- max(treino) <= min(validacao): **{ok_tv}** (treino_max={train_max}, val_min={val_min})")
    else:
        print("- validacao vazia: ignorar checagem treino/val.")
    if len(parts[1][1]) > 0 and len(parts[2][1]) > 0:
        ok_vte = val_max <= test_min
        print(f"- max(validacao) <= min(teste): **{ok_vte}** (val_max={val_max}, test_min={test_min})")
    elif len(parts[2][1]) == 0:
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
    print(f"- pandas {pd.__version__}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
