# Changelog — M03 / T033: rede NumPy alinhada a `temperature_C` (T030)

**Data:** 2026-05-02

## Resumo

O notebook [`notebooks/neural_network_numpy_training.ipynb`](../../notebooks/neural_network_numpy_training.ipynb) passou de **classificação binária** (`rain_label`, BCE + sigmoid) para **regressão** em **`temperature_C`**, alinhado a [`docs/metricas.md`](../metricas.md) (**T030**): perda **MSE**, saída **linear**, métricas **MAE**, **RMSE** e **R²** em val/teste. As features numéricas **não** incluem o alvo (evita fuga de rótulo).

## Motivação

- Protocolo de avaliação e restantes modelos M03 usam regressão em `temperature_C`.
- A configuração anterior (`TARGET = "rain_label"`) contradizia T030 e gerava métricas de classificação não comparáveis ao baseline de regressão.

## O que mudou

| Caminho | Alteração |
|---------|-----------|
| `notebooks/neural_network_numpy_training.ipynb` | `TARGET = "temperature_C"`; remoção de `temperature_C` de `NUM_COLS`; `mse()` em vez de `bce`; última camada **linear**; `backward` com gradiente da MSE média; `evaluate()` devolve MAE, RMSE, R² (agregação por batches). |
| `storyline/tasks/T033-rede-neural.md` | Evidence atualizada com ligação a esta entrada. |

## Como verificar

1. `data/Indian_Weather_Dataset.parquet` presente.
2. Abrir o notebook; executar por ordem. É esperado `mse=...` por época e linhas `VAL` / `TEST` com três números **finitos** (MAE, RMSE, R²).

## Riscos / limites

- Treino numérico instável: reduzir `LR` ou épocas se MSE explodir.
- R² no conjunto de val/teste usa a definição clássica com média de **y** no mesmo conjunto.

## Relacionado

- [2026-04-28-m03-notebook-train-numpy-nn.md](2026-04-28-m03-notebook-train-numpy-nn.md) (versão inicial BCE / `rain_label`).
- [T033](../../storyline/tasks/T033-rede-neural.md), [T030 / métricas](../metricas.md).
