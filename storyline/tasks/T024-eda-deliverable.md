# T024 — EDA entregável (figuras + insights)

```yaml
id: T024
story: S02
milestone: M02
status: Todo
depends_on: [T021, T022, T023]
artifacts:
  - notebooks/eda.ipynb   # caminho sugerido; ajustar ao repo
  - figuras exportadas (png) opcional
```

## Objetivo

Produzir **análise exploratória** com visualizações (distribuições, sazonalidade, correlações, geografia agregada se fizer sentido) e **insights em texto** que guiem modelagem.

## Checklist

- [ ] Cobrir pelo menos: distribuição do alvo, 2–3 relações feature–alvo, correlação entre preditores.
- [ ] Explorar dimensão temporal (`hour`, `month`, `datetime`).
- [ ] Listar 3–5 **insights acionáveis** para a Parte 3.
- [ ] Referenciar caminhos de figuras no repositório ou no notebook.

## Evidence

- Link para notebook ou relatório Markdown/PDF.

## Links

- Story: [../storys/S02-parte2-eda-preprocessamento.md](../storys/S02-parte2-eda-preprocessamento.md)
- Milestone: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
