# `rain_label_counts.py` — Frequências do alvo (T023)

## Objetivo

Ler apenas a coluna **`rain_label`** (ou outra passada em `--column`) do Parquet e imprimir uma **tabela Markdown** com contagem e **% do total** (com base na soma retornada por `pyarrow.compute.value_counts`). Serve para documentar desequilíbrio em [`docs/imbalance.md`](../docs/imbalance.md).

## Onde corre

No **host**, com `pip install -r requirements.txt` (só **pyarrow**).

## Uso

```powershell
python scripts\rain_label_counts.py -i data\Indian_Weather_Dataset.parquet
```

Outra coluna categórica:

```powershell
python scripts\rain_label_counts.py -i data\Indian_Weather_Dataset.parquet --column state
```

## Saída

Copie o bloco Markdown do terminal e cole na secção **“Distribuição empírica”** de `docs/imbalance.md`, substituindo a tabela antiga se já existir.

## Ver também

- [imbalance.md](../docs/imbalance.md) (T023)
- [profile_parquet.md](profile_parquet.md)
