# T020 — Dataset, variável alvo e aprovação do professor

```yaml
id: T020
story: S02
milestone: M02
status: Done
depends_on: []
artifacts:
  - organization/evidencias/aprovacao.md   # opcional: criar pasta se a equipe usar
  - nota de tamanho do arquivo (>1 GB)
```

## Objetivo

Formalizar o uso do **Indian Weather** (ou dataset aprovado), definir **variável alvo** e tipo de tarefa (**regressão** ou **classificação**), e registrar **aprovação do professor**.

## Checklist

- [x] Citar caminho e tamanho em disco do dataset (ex.: `data/Indian_Weather_Dataset.parquet`).
- [x] Definir alvo (ex.: `rain_label`, `precip_mm`) e métrica principal planejada.
- [x] Registrar data e forma da aprovação (e-mail, Teams, folha assinada — conforme política).
- [x] Se ainda pendente, marcar status **Blocked** e descrever próximo passo. *(N/A — aprovado.)*

## Evidence

- Registo formal: [organization/evidencias/aprovacao.md](../../organization/evidencias/aprovacao.md) (dataset, tamanhos, alvo `rain_label`, classificação, métrica F1 macro, aprovação docente 2026-04-22).

## Links

- Story: [../storys/S02-parte2-eda-preprocessamento.md](../storys/S02-parte2-eda-preprocessamento.md)
- Milestone: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
