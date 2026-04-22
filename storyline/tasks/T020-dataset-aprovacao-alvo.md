# T020 — Dataset, variável alvo e aprovação do professor

```yaml
id: T020
story: S02
milestone: M02
status: Todo
depends_on: []
artifacts:
  - organization/evidencias/aprovacao.md   # opcional: criar pasta se a equipe usar
  - nota de tamanho do arquivo (>1 GB)
```

## Objetivo

Formalizar o uso do **Indian Weather** (ou dataset aprovado), definir **variável alvo** e tipo de tarefa (**regressão** ou **classificação**), e registrar **aprovação do professor**.

## Checklist

- [ ] Citar caminho e tamanho em disco do dataset (ex.: `data/Indian_Weather_Dataset.parquet`).
- [ ] Definir alvo (ex.: `rain_label`, `precip_mm`) e métrica principal planejada.
- [ ] Registrar data e forma da aprovação (e-mail, Teams, folha assinada — conforme política).
- [ ] Se ainda pendente, marcar status **Blocked** e descrever próximo passo.

## Evidence

- Texto curto “Aprovado em … por …” ou anexo referenciado.

## Links

- Story: [../storys/S02-parte2-eda-preprocessamento.md](../storys/S02-parte2-eda-preprocessamento.md)
- Milestone: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
