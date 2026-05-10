# T033 — Modelo de rede neural

```yaml
id: T033
story: S03
milestone: M03
status: Todo
depends_on: [T030]
artifacts:
  - notebook PySpark MLlib — [../../notebooks/neural_network_pyspark_mllib.ipynb](../../notebooks/neural_network_pyspark_mllib.ipynb)
```

## Objetivo

Treinar uma **rede neural** para o mesmo alvo, com arquitetura e treino **documentados** (camadas, ativações, épocas, batch, early stopping se houver).

## Checklist

- [ ] Diagrama ou lista de camadas e unidades.
- [ ] Função de perda alinhada à tarefa.
- [ ] Registrar tempo aproximado de treino e hardware.
- [ ] Métricas no val/teste no protocolo de **T030**.

## Evidence

- **Principal (PySpark / MLlib):** [../../notebooks/neural_network_pyspark_mllib.ipynb](../../notebooks/neural_network_pyspark_mllib.ipynb) — `MultilayerPerceptronClassifier`, métricas MAE/RMSE/R² em °C após discretização do alvo (ver changelog). Changelog: [../../docs/changelog/2026-05-07-m03-t033-pyspark-mllib-mlp.md](../../docs/changelog/2026-05-07-m03-t033-pyspark-mllib-mlp.md).
- **Histórico (NumPy + PyArrow):** [../../notebooks/neural_network_numpy_training.ipynb](../../notebooks/neural_network_numpy_training.ipynb); regressão `temperature_C` — [../../docs/changelog/2026-05-02-m03-t033-neural-network-temperature-regression.md](../../docs/changelog/2026-05-02-m03-t033-neural-network-temperature-regression.md); BCE antigo — [../../docs/changelog/2026-04-28-m03-notebook-train-numpy-nn.md](../../docs/changelog/2026-04-28-m03-notebook-train-numpy-nn.md).
- Curva de loss opcional; métricas finais obrigatórias (completar checklist T033 ao fechar M03).

## Links

- Story: [../storys/S03-parte3-modelos-avaliacao.md](../storys/S03-parte3-modelos-avaliacao.md)
- Milestone: [../milestones/M03-modelagem-avaliacao.md](../milestones/M03-modelagem-avaliacao.md)
