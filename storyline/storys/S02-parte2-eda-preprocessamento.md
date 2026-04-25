# S02 — Parte 2: Análise de dados (EDA + pré-processamento)

```yaml
id: S02
milestone_primary: M02
status: Done
```

## Enunciado (referência)

> Parte 2: Tarefa de Analise de dados — 5 pontos  
> Seleção de dados (Kaggle ou similar), regressão ou classificação; **> 1 GB**; aprovação do professor.  
> Pré-processamento, tratamento de desequilíbrio de classes, EDA com insights e distribuição das classes.

Fonte: [core.md](../../core.md).

## Problema / objetivo da story

Definir formalmente a **tarefa de aprendizado** (alvo e tipo), obter **aprovação**, preparar dados com **pré-processamento** sólido e produzir **EDA** que sustente decisões da Parte 3.

## Critérios de aceite

- Dataset adequado à tarefa com **mais de 1 GB** (citar tamanho em disco e fonte).
- **Aprovação do professor** registrada.
- **Pré-processamento** documentado e reproduzível.
- **Desequilíbrio de classes** tratado ou justificado como N/A (ex.: regressão).
- **EDA** com visualizações e interpretação escrita.

## Dados de referência

- Parquet: `data/Indian_Weather_Dataset.parquet`

## Definition of Done

- [x] Alvo e tipo de problema definidos e aprovados (**T020** Done).
- [x] Split e validação sem vazamento temporal documentados (**T021** Done).
- [x] Pipeline de features acordado (**T022** Done).
- [x] Plano de imbalance completo ou N/A justificado (**T023** Done).
- [x] Relatório/notebook de EDA entregue (**T024** Done).

## Índice de tasks

| Task ID | Título | Owner | Status |
|---------|--------|-------|--------|
| T020 | Dataset, alvo e aprovação do professor | | Done |
| T021 | Split reproduzível e checagem de vazamento | | Done |
| T022 | Especificação do pré-processamento | | Done |
| T023 | Desequilíbrio de classes | | Done |
| T024 | EDA e figuras | | Done |

Arquivos: [../tasks/T020-dataset-aprovacao-alvo.md](../tasks/T020-dataset-aprovacao-alvo.md), [../tasks/T021-split-temporal-leakage.md](../tasks/T021-split-temporal-leakage.md), [../tasks/T022-preprocessamento-pipeline.md](../tasks/T022-preprocessamento-pipeline.md), [../tasks/T023-desequilibrio-classes.md](../tasks/T023-desequilibrio-classes.md), [../tasks/T024-eda-deliverable.md](../tasks/T024-eda-deliverable.md).

## Milestones relacionados

- Principal: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
