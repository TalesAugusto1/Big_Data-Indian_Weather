# Changelog: M02 — Script `profile_parquet.py` (perfil PyArrow)

**Data:** 2026-04-26  
**Área:** M02 / suporte a T022 e T024  
**Relação:** [T022](../../storyline/tasks/T022-preprocessamento-pipeline.md), [docs/preprocessamento.md](../../docs/preprocessamento.md)

## Resumo

Novo script **[`scripts/profile_parquet.py`](../../scripts/profile_parquet.py)** (só **PyArrow**): lê um Parquet **coluna a coluna** e imprime tabela Markdown com tipo, linhas, nulos, % nulos, distintos (com amostra configurável), min/max quando aplicável. Documentação em [`scripts/profile_parquet.md`](../../scripts/profile_parquet.md). O [`docs/preprocessamento.md`](../../docs/preprocessamento.md) ganhou a secção **Perfil empírico** com o fluxo recomendado (correr script → colar medições → ajustar o pipeline).

## Motivação

Fundamentar missing e cardinalidade com **números reais** sobre o dataset, sem **pandas** nem **scikit-learn**, alinhado às restrições da turma.

## O que mudou

| Item | Detalhe |
|------|---------|
| [scripts/profile_parquet.py](../../scripts/profile_parquet.py) | Novo |
| [scripts/profile_parquet.md](../../scripts/profile_parquet.md) | Novo |
| [scripts/README.md](../../scripts/README.md) | Tabela + ligação útil |
| [docs/preprocessamento.md](../../docs/preprocessamento.md) | Secção perfil empírico + ligação em “Ligações” |
| [docs/README.md](../../docs/README.md) | Entrada M02 para `profile_parquet.md` |
| [storyline/tasks/T022-preprocessamento-pipeline.md](../../storyline/tasks/T022-preprocessamento-pipeline.md) | Evidence atualizada |

## Como verificar

```powershell
pip install -r requirements.txt
python scripts\profile_parquet.py -i data\Indian_Weather_Dataset.parquet
```

Deve aparecer uma tabela Markdown no stdout.
