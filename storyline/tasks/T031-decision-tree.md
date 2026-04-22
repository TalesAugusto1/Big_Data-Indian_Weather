# T031 — Modelo Decision Tree

```yaml
id: T031
story: S03
milestone: M03
status: Todo
depends_on: [T030]
artifacts:
  - notebooks/modelos.ipynb   # ou scripts/train_decision_tree.py
```

## Objetivo

Treinar **árvore de decisão** adequada ao tipo de tarefa (regressor ou classificador), com hiperparâmetros documentados e avaliação no mesmo protocolo de **T030**.

## Checklist

- [ ] Escolher implementação (scikit-learn, Spark MLlib, etc.).
- [ ] Registrar profundidade, critério de split, `min_samples_leaf` (ou equivalentes).
- [ ] Métricas no val/teste conforme protocolo.
- [ ] Salvar artefato do modelo se necessário para demo.

## Evidence

- Tabela com hiperparâmetros e métricas.

## Links

- Story: [../storys/S03-parte3-modelos-avaliacao.md](../storys/S03-parte3-modelos-avaliacao.md)
- Milestone: [../milestones/M03-modelagem-avaliacao.md](../milestones/M03-modelagem-avaliacao.md)
