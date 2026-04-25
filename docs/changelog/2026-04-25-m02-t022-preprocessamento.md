# Changelog: M02 / T022 — Especificação do pipeline de pré-processamento

**Data:** 2026-04-25  
**Área:** Storyline M02 / S02 / Parte 2  
**Storyline:** [T022](../../storyline/tasks/T022-preprocessamento-pipeline.md)

## Resumo

Documento **[docs/preprocessamento.md](../../docs/preprocessamento.md)** com a especificação do pipeline: tabela **coluna → tipo → transformação**, tratamento de **missing**, **TOP-K + `__OTHER__`** para alta cardinalidade (`city`, `crops`), **standardização** com estatísticas do **treino**, regra explícita **fit só em treino / transform em val e teste**, formato de saída em **Parquet** sob `data/processed/`. Alinhado ao alvo **`rain_label`** e ao split temporal da **T021**; implementação futura sem **pandas** / **scikit-learn** (Spark / PyArrow).

## Motivação

Fechar **T022** como base para **T023** (desequilíbrio) e **T024** (EDA), cumprindo critério de saída do marco M02 sobre pipeline descrito.

## O que mudou

| Item | Detalhe |
|------|---------|
| [docs/preprocessamento.md](../../docs/preprocessamento.md) | Novo: especificação completa do pipeline |
| [docs/README.md](../../docs/README.md) | Secção M02 com ligações a preprocessamento, T020, T021 |
| [storyline/tasks/T022-preprocessamento-pipeline.md](../../storyline/tasks/T022-preprocessamento-pipeline.md) | `Done`, checklist, Evidence |
| [storyline/storys/S02-parte2-eda-preprocessamento.md](../../storyline/storys/S02-parte2-eda-preprocessamento.md) | T022 **Done**; DoD pipeline marcado |

## Como verificar

1. Ler [docs/preprocessamento.md](../../docs/preprocessamento.md).
2. Confirmar no ficheiro da task T022 que `status: Done` e Evidence apontam para o mesmo documento.

## Follow-ups

- **T023:** plano de desequilíbrio para `rain_label`.
- **T024:** EDA e eventual script Spark/PyArrow que materialize `data/processed/*.parquet` conforme esta especificação.
