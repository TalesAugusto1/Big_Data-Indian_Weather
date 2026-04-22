# M02 — Dados aprovados e análise

```yaml
id: M02
status: Doing
```

## Objetivo

**Seleção e aprovação** do dataset e do alvo (regressão ou classificação), **pré-processamento**, **tratamento de desequilíbrio** (quando aplicável), **EDA** com insights e distribuição do alvo/classes. Atender pré-requisito de **> 1 GB** de dados.

## Datas-alvo

Ajustar ao calendário do curso e à janela de apresentações (11/05, 13/05, 25/05, 27/05).

## Critérios de saída

- Registro explícito da **aprovação do professor** (ou status bloqueado com evidência de solicitação).
- **Alvo** e tipo de tarefa definidos (regressão vs classificação).
- **Split reproduzível** documentado (recomendado: split temporal por `datetime` para evitar vazamento).
- Pipeline de pré-processamento descrito (encoding, escalonamento, missing).
- Plano de desequilíbrio de classes **ou** justificativa N/A para regressão.
- EDA entregue (notebook ou relatório) com figuras e conclusões escritas.

## Storys ligadas

- [S02 — Parte 2: EDA e pré-processamento](../storys/S02-parte2-eda-preprocessamento.md)

## Tasks ligadas

| ID | Título | Arquivo |
|----|--------|---------|
| T020 | Dataset, alvo e aprovação | [../tasks/T020-dataset-aprovacao-alvo.md](../tasks/T020-dataset-aprovacao-alvo.md) |
| T021 | Split e checagem de vazamento | [../tasks/T021-split-temporal-leakage.md](../tasks/T021-split-temporal-leakage.md) |
| T022 | Especificação de pré-processamento | [../tasks/T022-preprocessamento-pipeline.md](../tasks/T022-preprocessamento-pipeline.md) |
| T023 | Desequilíbrio de classes | [../tasks/T023-desequilibrio-classes.md](../tasks/T023-desequilibrio-classes.md) |
| T024 | EDA e figuras | [../tasks/T024-eda-deliverable.md](../tasks/T024-eda-deliverable.md) |
