# T021 — Split reproduzível e checagem de vazamento

```yaml
id: T021
story: S02
milestone: M02
status: Done
depends_on: [T020]
artifacts:
  - notebook ou script com seed e regras de split
```

## Objetivo

Definir **treino/validação/teste** de forma **reprodutível**, priorizando **split temporal** por `datetime` (ou justificar outro esquema) e documentar checagens contra **data leakage**.

## Checklist

- [x] Descrever colunas usadas para ordenar e cortar no tempo (`datetime`; ordenação mergesort ascendente).
- [x] Fixar **seed** e versão de biblioteca se necessário para reprodutibilidade (`--seed` por defeito 42; pyarrow impresso no output).
- [x] Listar features que não podem existir no treino se calculadas com futuro (secção anti-leakage no output do script).
- [x] Tamanhos aproximados de cada split (tabela Markdown no stdout).

## Evidence

- Script: [`scripts/split_temporal.py`](../../scripts/split_temporal.py) — lê só `datetime`, frações 70/15/15 configuráveis, tabela de contagens e limites temporais, checagens de fronteira e bullets de leakage.
- Documentação: [`scripts/split_temporal.md`](../../scripts/split_temporal.md).
- Para revisão: executar `python scripts/split_temporal.py -i <path>` e anexar/guardar o output (tabela + checagens).

## Links

- Story: [../storys/S02-parte2-eda-preprocessamento.md](../storys/S02-parte2-eda-preprocessamento.md)
- Milestone: [../milestones/M02-dados-aprovados-eda.md](../milestones/M02-dados-aprovados-eda.md)
