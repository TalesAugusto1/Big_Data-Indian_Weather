# T023 — Tratamento de desequilíbrio de classes (ou N/A)

```yaml
id: T023
story: S02
milestone: M02
status: Done
depends_on: [T020, T022]
artifacts:
  - docs/imbalance.md ou seção no notebook
```

## Objetivo

Se a tarefa for **classificação**, analisar distribuição do alvo e aplicar ou justificar estratégia (**class weights**, **resampling**, **threshold tuning**, etc.). Se for **regressão**, documentar **N/A** com uma frase objetiva.

## Checklist

- [x] Gráfico ou tabela de frequências por classe (classificação) — tabela em [`docs/imbalance.md`](../../docs/imbalance.md) + script [`scripts/rain_label_counts.py`](../../scripts/rain_label_counts.py).
- [x] Decisão final da estratégia e parâmetros (ex.: `class_weight='balanced'`) — pesos no **Spark** no treino; threshold secundário na validação (ver `imbalance.md`).
- [x] Para regressão: declarar N/A e focar em outliers/skew se relevante — **N/A**: o alvo acordado é **classificação** (`rain_label`, T020).

## Evidence

- Documento: [`docs/imbalance.md`](../../docs/imbalance.md) (frequências reais, interpretação PT-BR, estratégia e o que não fazer).
- Script de contagens: [`scripts/rain_label_counts.py`](../../scripts/rain_label_counts.py) e [`scripts/rain_label_counts.md`](../../scripts/rain_label_counts.md).

## Links

- Story: [../storys/S02-parte2-eda-preprocessamento.md](../storys/S02-parte2-eda-preprocessamento.md)
- Milestone: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
