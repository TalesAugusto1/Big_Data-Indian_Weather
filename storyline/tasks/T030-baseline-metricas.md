# T030 — Baseline e protocolo de avaliação

```yaml
id: T030
story: S03
milestone: M03
status: Todo
depends_on: [T024]
artifacts:
  - docs/metricas.md ou seção no notebook de modelagem
```

## Objetivo

Definir **métricas principais e secundárias** coerentes com regressão ou classificação, registrar um **baseline simples** (ex.: média, majority class) e garantir que **todos os modelos** usem o **mesmo split** da S02.

## Checklist

- [ ] Escolher métrica principal (MAE/RMSE ou F1/AUC, etc.) e justificar em 1 parágrafo.
- [ ] Implementar baseline trivial reproduzível.
- [ ] Congelar seeds e caminhos de dados usados na Parte 3.
- [ ] Definir limite de tempo ou amostra se treino for inviável em laptop (com aprovação da equipe/docente).

## Evidence

- Números do baseline no conjunto de validação/teste.

## Links

- Story: [../storys/S03-parte3-modelos-avaliacao.md](../storys/S03-parte3-modelos-avaliacao.md)
- Milestone: [../milestones/M03-modelagem-avaliacao.md](../milestones/M03-modelagem-avaliacao.md)
