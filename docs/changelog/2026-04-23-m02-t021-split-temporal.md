# Changelog: M02 / T021 — Split temporal e anti-leakage

**Data:** 2026-04-23  
**Área:** Storyline M02 / S02 / Parte 2  
**Storyline:** [T021](../../storyline/tasks/T021-split-temporal-leakage.md)

## Resumo

Script **`split_temporal.py`** no host: lê apenas a coluna **`datetime`** do Parquet, ordena de forma estável com **PyArrow**, aplica frações **treino / validação / teste** (por defeito 0,70 / 0,15 / 0,15), imprime tabela Markdown com contagens e limites temporais, checagens de fronteira e lista de **riscos de data leakage**. Implementação sem pandas.

## Motivação

Fechar **T021** como pré-requisito de **T022** (pré-processamento) e **T024** (EDA), com regra de split documentada e reprodutível.

## O que mudou

| Item | Detalhe |
|------|---------|
| [requirements.txt](../../requirements.txt) | Mantido só com `pyarrow>=14.0.0` (sem pandas) |
| [scripts/split_temporal.py](../../scripts/split_temporal.py) | CLI, split temporal, output Markdown + leakage |
| [scripts/split_temporal.md](../../scripts/split_temporal.md) | Documentação do script |
| [scripts/README.md](../../scripts/README.md) | Entrada na tabela de scripts |
| [storyline/tasks/T021-split-temporal-leakage.md](../../storyline/tasks/T021-split-temporal-leakage.md) | `Done`, checklist, Evidence |
| [storyline/storys/S02-parte2-eda-preprocessamento.md](../../storyline/storys/S02-parte2-eda-preprocessamento.md) | T021 na tabela **Done**; DoD T021 |

## Como verificar

```powershell
pip install -r requirements.txt
python scripts\split_temporal.py -i data\Indian_Weather_Dataset.parquet
```

Confirmar tabela de contagens e mensagens `max(treino) <= min(validacao)` quando aplicável.

## Follow-ups

- T022: pipeline de features encaixado no split (fit só em treino).
- Opcional: materializar ficheiros train/val/test em Parquet numa pasta `data/splits/` (não incluído neste PR).
