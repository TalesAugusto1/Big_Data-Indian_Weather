# T021 — Split reproduzível e checagem de vazamento

```yaml
id: T021
story: S02
milestone: M02
status: Todo
depends_on: [T020]
artifacts:
  - notebook ou script com seed e regras de split
```

## Objetivo

Definir **treino/validação/teste** de forma **reprodutível**, priorizando **split temporal** por `datetime` (ou justificar outro esquema) e documentar checagens contra **data leakage**.

## Checklist

- [ ] Descrever colunas usadas para ordenar e cortar no tempo.
- [ ] Fixar **seed** e versão de biblioteca se necessário para reprodutibilidade.
- [ ] Listar features que não podem existir no treino se calculadas com futuro (normalização global, etc.).
- [ ] Tamanhos aproximados de cada split.

## Evidence

- Tabela com contagens por split ou link para célula do notebook.

## Links

- Story: [../storys/S02-parte2-eda-preprocessamento.md](../storys/S02-parte2-eda-preprocessamento.md)
- Milestone: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
