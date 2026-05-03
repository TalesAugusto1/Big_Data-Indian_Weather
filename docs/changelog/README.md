# Entradas de changelog

Esta pasta regista **desenvolvimento relevante** no repositório (funcionalidades, ferramentas, alterações estruturais). Cada entrada é um ficheiro Markdown próprio para facilitar navegação e ligações a PRs ou tarefas.

## Convenção

- **Um ficheiro por alteração maior** (ou por funcionalidade coesa), nome `YYYY-MM-DD-slug-curto.md` com a data em que o trabalho foi integrado (ou a data principal do commit).
- Incluir: **resumo**, **motivação**, **o que mudou** (caminhos, APIs), **como correr** ou verificar, **dependências** e **follow-ups** se existirem.
- As entradas novas listam-se abaixo (mais recentes primeiro).

## Índice

| Data | Slug | Resumo |
|------|------|--------|
| 2026-05-02 | [m03-t033-neural-network-temperature-regression](2026-05-02-m03-t033-neural-network-temperature-regression.md) | M03 / T033: `neural_network_numpy_training.ipynb` — alvo `temperature_C`, MSE + saída linear, MAE/RMSE/R² (T030); sem `temperature_C` nas features |
| 2026-05-02 | [m03-t031-decision-tree-notebook-robustness](2026-05-02-m03-t031-decision-tree-notebook-robustness.md) | M03 / T031: `setuptools`; `decision_tree.ipynb` (JAVA_HOME, `SPARK_MASTER`, `_reset_spark_if_stale`, `coalesce`, env driver/shuffle); Compose `notebook` (`SPARK_DRIVER_MEMORY`, `DTR_NOTEBOOK_MAX_ROWS`, `persist` DISK_ONLY); README / `docker/README` troubleshooting #7–#8; comentários `docker/hadoop.env` |
| 2026-04-28 | [m03-notebook-train-numpy-nn](2026-04-28-m03-notebook-train-numpy-nn.md) | M03 / T033: `notebooks/neural_network_numpy_training.ipynb` — MLP NumPy+PyArrow, split T021, path robusto, correção loss `nan` |
| 2026-04-30 | [m03-t031-decision-tree-eda-regressao](2026-04-30-m03-t031-decision-tree-eda-regressao.md) | M03 / T031: `decision_tree.ipynb` (Spark DecisionTreeRegressor + métricas T030); EDA ampliado com figuras temporais, correlações e insights para `temperature_C` |
| 2026-04-27 | [m03-t030-regressao-temperature](2026-04-27-m03-t030-regressao-temperature.md) | M03 / T030: baseline migrado para regressao em `temperature_C` com MAE/RMSE/R2 e comparativo sazonal (`hour`, `month`, `hour+month`) |
| 2026-04-27 | [m02-t023-imbalance](2026-04-27-m02-t023-imbalance.md) | M02 / T023: `docs/imbalance.md` + `rain_label_counts.py` (frequências `rain_label`, estratégia Spark) |
| 2026-04-26 | [m03-t030-baseline-metricas](2026-04-26-m03-t030-baseline-metricas.md) | M03 / T030: docs/metricas.md + calcula_base.py (Métrica F1, Split 70/30, Baseline 0.9540) |
| 2026-04-26 | [m02-profile-parquet](2026-04-26-m02-profile-parquet.md) | M02: `profile_parquet.py` (PyArrow) — nulos, distintos, min/max; ligação na T022/preprocessamento |
| 2026-04-25 | [m02-t022-preprocessamento](2026-04-25-m02-t022-preprocessamento.md) | M02 / T022: `docs/preprocessamento.md` — pipeline, fit treino, Parquet `data/processed/` |
| 2026-04-24 | [m02-t021-split-pyarrow-only](2026-04-24-m02-t021-split-pyarrow-only.md) | M02 / T021: refactor `split_temporal.py` só PyArrow; removido pandas do `requirements.txt` |
| 2026-04-23 | [m02-t021-split-temporal](2026-04-23-m02-t021-split-temporal.md) | M02 / T021: `split_temporal.py`, split 70/15/15 por `datetime`, anti-leakage |
| 2026-04-22 | [m02-t024-eda-notebook](2026-04-22-m02-t024-eda-notebook.md) | M02 / T024: `notebooks/eda.ipynb` (PyArrow + Matplotlib), `notebooks/figuras/`, dependências |
| 2026-04-22 | [m02-t020-dataset-aprovacao](2026-04-22-m02-t020-dataset-aprovacao.md) | M02 / T020: evidência de aprovação, alvo `rain_label`, critério >1 GB (CSV+Parquet) |
| 2026-04-21 | [t012-dataset-smoke](2026-04-21-t012-dataset-smoke.md) | Mount `./data` no Spark + smoke Parquet (M01 / T012) |
| 2026-04-21 | [docker-compose-m01](2026-04-21-docker-compose-m01.md) | `docker-compose.yml` + `docker/hadoop.env` + health checks (M01 / T011) |
| 2026-04-21 | [stack-apache-m01](2026-04-21-stack-apache-m01.md) | Documentação do stack Docker Apache (HDFS, YARN, Spark) para M01 / T010 (`docs/stack-apache.md`) |
| 2026-04-21 | [csv-to-parquet-streaming](2026-04-21-csv-to-parquet-streaming.md) | Streaming de CSV para Parquet com PyArrow (`scripts/csv_to_parquet.py`) |

## Relacionado

- Índice da documentação: [../README.md](../README.md).
- Runbook na raiz: [README.md](../../README.md) (início rápido, venv, flags de `csv_to_parquet.py`).
- Âmbito da disciplina: [core.md](../../core.md).
- Tarefas: [storyline/README.md](../../storyline/README.md).
