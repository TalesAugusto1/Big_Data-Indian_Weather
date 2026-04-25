# T022 — Especificação do pipeline de pré-processamento

```yaml
id: T022
story: S02
milestone: M02
status: Done
depends_on: [T021]
artifacts:
  - docs/preprocessamento.md ou notebook
```

## Objetivo

Documentar transformações: **missing values**, **encoding** de categóricas (`state`, `city`, `crops`, etc.), **escalonamento** de numéricas para modelos lineares/NN, e persistência do **pipeline** (fit no treino apenas).

## Checklist

- [x] Lista de colunas: tipo → transformação.
- [x] Estratégia para textos de alta cardinalidade (agrupar, hash, target encoding — com cuidado a leakage).
- [x] Onde o pipeline é **fit** (somente treino) e **transform** (val/teste).
- [x] Formato de saída (ex.: Parquet particionado, Delta, CSV interno).

## Evidence

- Especificação completa: [docs/preprocessamento.md](../../docs/preprocessamento.md) (tabela coluna→transformação, TOP-K + `__OTHER__`, fit/transform, caminhos `data/processed/*.parquet`, restrição sem pandas/sklearn; secção de **perfil empírico** com [`scripts/profile_parquet.py`](../../scripts/profile_parquet.py)).

## Links

- Story: [../storys/S02-parte2-eda-preprocessamento.md](../storys/S02-parte2-eda-preprocessamento.md)
- Milestone: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
