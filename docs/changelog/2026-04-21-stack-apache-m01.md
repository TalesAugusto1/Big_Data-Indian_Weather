# Changelog: documentação do stack Apache (M01 / T010)

**Data:** 2026-04-21  
**Área:** documentação / infraestrutura (Parte 1)  
**Artefato:** [docs/stack-apache.md](../stack-apache.md)

## Resumo

Documentada a **arquitetura alvo** do ambiente Big Data em Docker: **HDFS + YARN + Apache Spark** com imagens **bde2020** e **tags fixas** (Hadoop `2.0.0-hadoop3.2.1-java8`, Spark `3.2.1-hadoop3.2`), tabela de serviços, topologia (mermaid) e alternativas rejeitadas.

## Motivação

Cumprir a **T010** do [storyline](../../storyline/README.md): decisão explícita do ecossistema **Apache** antes de implementar o `docker compose` na **T011** e o smoke test de dados na **T012**.

## O que mudou

| Item | Detalhe |
|------|---------|
| Novo arquivo | `docs/stack-apache.md` — requisitos, tabela imagem/tag, diagrama, ponteiros para T011/T012 |
| Storyline | [storyline/tasks/T010-docker-compose-stack.md](../../storyline/tasks/T010-docker-compose-stack.md) → `status: Done`; [S01](../../storyline/storys/S01-parte1-ambiente-docker-apache.md) tabela T010 → Done |

## Como verificar

- Abrir [docs/stack-apache.md](../stack-apache.md) e confirmar tabela com pins e nota de validação com o docente.
- Conferir Evidence em T010.

## Próximos passos

- **T011:** `docker-compose.yml`, redes, variáveis `bde2020`, health checks.
- **T012:** mount/ingestão do Parquet e leitura mínima (ex.: Spark `count`).

## Riscos

- Imagens `bde2020` são antigas (comunidade); aceitável para laboratório; trocar por Bitnami/official se o curso exigir.
