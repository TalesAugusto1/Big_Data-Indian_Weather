# T032 — Linear Regression ou Logistic Regression

```yaml
id: T032
story: S03
milestone: M03
status: Todo
depends_on: [T030]
artifacts:
  - notebook ou script do modelo linear
```

## Objetivo

Treinar **Linear Regression** (regressão) ou **Logistic Regression** (classificação), alinhado ao alvo definido em **T020**, com **regularização** e pré-processamento compatíveis (escala de features).

## Checklist

- [ ] Confirmar alinhamento regressão ↔ Linear / classificação ↔ Logística.
- [ ] Documentar penalização (`l2`, `l1`, `elasticnet`) e solver.
- [ ] Avaliar com o mesmo protocolo de **T030**.
- [ ] Se coeficientes forem interpretados, anotar limites (correlação vs causalidade).

## Evidence

- Métricas + nota de 2 linhas sobre interpretação opcional.

## Links

- Story: [../storys/S03-parte3-modelos-avaliacao.md](../storys/S03-parte3-modelos-avaliacao.md)
- Milestone: [../milestones/M03-modelagem-avaliacao.md](../milestones/M03-modelagem-avaliacao.md)
