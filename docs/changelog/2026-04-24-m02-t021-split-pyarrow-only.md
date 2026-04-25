# Changelog: M02 / T021 — Split temporal só com PyArrow (sem pandas)

**Data:** 2026-04-24  
**Área:** Storyline M02 / S02 / Parte 2  
**Storyline:** [T021](../../storyline/tasks/T021-split-temporal-leakage.md)

## Resumo

O script [`scripts/split_temporal.py`](../../scripts/split_temporal.py) foi **refatorado** para não usar **pandas** nem **scikit-learn**, em linha com a orientação da disciplina. O split temporal por `datetime` passa a depender apenas de **PyArrow** (`read_table`, `compute.sort_indices`, `compute.take`, `compute.min_max`). A dependência `pandas` foi **removida** de [`requirements.txt`](../../requirements.txt).

## Motivação

Cumprir restrição explícita da turma/docente: **não utilizar pandas nem scikit-learn** neste fluxo.

## O que mudou

| Item | Detalhe |
|------|---------|
| [requirements.txt](../../requirements.txt) | Removido `pandas>=2.0.0`; mantém `pyarrow>=14.0.0` |
| [scripts/split_temporal.py](../../scripts/split_temporal.py) | Implementação só PyArrow |
| [scripts/split_temporal.md](../../scripts/split_temporal.md) | Documentação atualizada (pyarrow apenas) |
| [docs/changelog/2026-04-23-m02-t021-split-temporal.md](2026-04-23-m02-t021-split-temporal.md) | Texto alinhado com implementação sem pandas |
| [storyline/tasks/T021-split-temporal-leakage.md](../../storyline/tasks/T021-split-temporal-leakage.md) | Checklist: menção a versão **pyarrow** no output |

## Como verificar

```powershell
pip install -r requirements.txt
python scripts\split_temporal.py -i data\Indian_Weather_Dataset.parquet
```

Confirmar na saída a linha `pyarrow <versão>` e ausência de import/uso de pandas no código-fonte do script.

## Follow-ups

- T022 / EDA: se surgirem outras dependências proibidas, substituir por PyArrow / Spark conforme o enunciado.
