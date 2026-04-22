# Entradas de changelog

Esta pasta regista **desenvolvimento relevante** no repositório (funcionalidades, ferramentas, alterações estruturais). Cada entrada é um ficheiro Markdown próprio para facilitar navegação e ligações a PRs ou tarefas.

## Convenção

- **Um ficheiro por alteração maior** (ou por funcionalidade coesa), nome `YYYY-MM-DD-slug-curto.md` com a data em que o trabalho foi integrado (ou a data principal do commit).
- Incluir: **resumo**, **motivação**, **o que mudou** (caminhos, APIs), **como correr** ou verificar, **dependências** e **follow-ups** se existirem.
- As entradas novas listam-se abaixo (mais recentes primeiro).

## Índice

| Data | Slug | Resumo |
|------|------|--------|
| 2026-04-21 | [t012-dataset-smoke](2026-04-21-t012-dataset-smoke.md) | Mount `./data` no Spark + smoke Parquet (M01 / T012) |
| 2026-04-21 | [docker-compose-m01](2026-04-21-docker-compose-m01.md) | `docker-compose.yml` + `docker/hadoop.env` + health checks (M01 / T011) |
| 2026-04-21 | [stack-apache-m01](2026-04-21-stack-apache-m01.md) | Documentação do stack Docker Apache (HDFS, YARN, Spark) para M01 / T010 (`docs/stack-apache.md`) |
| 2026-04-21 | [csv-to-parquet-streaming](2026-04-21-csv-to-parquet-streaming.md) | Streaming de CSV para Parquet com PyArrow (`scripts/csv_to_parquet.py`) |

## Relacionado

- Índice da documentação: [../README.md](../README.md).
- Runbook na raiz: [README.md](../../README.md) (início rápido, venv, flags de `csv_to_parquet.py`).
- Âmbito da disciplina: [core.md](../../core.md).
- Tarefas: [storyline/README.md](../../storyline/README.md).
