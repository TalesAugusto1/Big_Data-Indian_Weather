# T022 — Especificação do pipeline de pré-processamento

```yaml
id: T022
story: S02
milestone: M02
status: Todo
depends_on: [T021]
artifacts:
  - docs/preprocessamento.md ou notebook
```

## Objetivo

Documentar transformações: **missing values**, **encoding** de categóricas (`state`, `city`, `crops`, etc.), **escalonamento** de numéricas para modelos lineares/NN, e persistência do **pipeline** (fit no treino apenas).

## Checklist

- [ ] Lista de colunas: tipo → transformação.
- [ ] Estratégia para textos de alta cardinalidade (agrupar, hash, target encoding — com cuidado a leakage).
- [ ] Onde o pipeline é **fit** (somente treino) e **transform** (val/teste).
- [ ] Formato de saída (ex.: Parquet particionado, Delta, CSV interno).

## Evidence

- Diagrama simples ou bullet list aceito; preferir link para código/notebook.

## Links

- Story: [../storys/S02-parte2-eda-preprocessamento.md](../storys/S02-parte2-eda-preprocessamento.md)
- Milestone: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
