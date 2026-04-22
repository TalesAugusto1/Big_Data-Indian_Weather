# T023 — Tratamento de desequilíbrio de classes (ou N/A)

```yaml
id: T023
story: S02
milestone: M02
status: Todo
depends_on: [T020, T022]
artifacts:
  - docs/imbalance.md ou seção no notebook
```

## Objetivo

Se a tarefa for **classificação**, analisar distribuição do alvo e aplicar ou justificar estratégia (**class weights**, **resampling**, **threshold tuning**, etc.). Se for **regressão**, documentar **N/A** com uma frase objetiva.

## Checklist

- [ ] Gráfico ou tabela de frequências por classe (classificação).
- [ ] Decisão final da estratégia e parâmetros (ex.: `class_weight='balanced'`).
- [ ] Para regressão: declarar N/A e focar em outliers/skew se relevante.

## Evidence

- Link para figura ou números copiados aqui após concluir a task.

## Links

- Story: [../storys/S02-parte2-eda-preprocessamento.md](../storys/S02-parte2-eda-preprocessamento.md)
- Milestone: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
