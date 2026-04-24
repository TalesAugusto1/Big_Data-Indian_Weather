# T024 — EDA entregável (figuras + insights)

```yaml
id: T024
story: S02
milestone: M02
status: Done
depends_on: [T021, T022, T023]
artifacts:
  - notebooks/eda.ipynb
  - notebooks/figuras/eda_*.png (geradas localmente ao executar o notebook)
```

## Objetivo

Produzir **análise exploratória** com visualizações (distribuições, sazonalidade, correlações, geografia agregada se fizer sentido) e **insights em texto** que guiem modelagem.

## Checklist

- [x] Cobrir pelo menos: distribuição do alvo, 2–3 relações feature–alvo, correlação entre preditores.
- [x] Explorar dimensão temporal (`hour`, `month`, `datetime`).
- [x] Listar 3–5 **insights acionáveis** para a Parte 3.
- [x] Referenciar caminhos de figuras no repositório ou no notebook.

## Evidence

- Notebook: [../../notebooks/eda.ipynb](../../notebooks/eda.ipynb) (PT-BR; PyArrow + Matplotlib; figuras em `notebooks/figuras/` com prefixo `eda_*.png`).

## Links

- Story: [../storys/S02-parte2-eda-preprocessamento.md](../storys/S02-parte2-eda-preprocessamento.md)
- Milestone: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
