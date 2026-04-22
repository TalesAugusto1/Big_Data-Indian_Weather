# Changelog: Docker Compose Hadoop + Spark (M01 / T011)

**Data:** 2026-04-21  
**Área:** infraestrutura / Parte 1  
**Ficheiros:** [docker-compose.yml](../../docker-compose.yml), [docker/hadoop.env](../../docker/hadoop.env), [docker/README.md](../../docker/README.md), [.env.example](../../.env.example)

## Resumo

Foi adicionado um **`docker-compose.yml`** na raiz com stack **bde2020**: HDFS (NameNode + DataNode), YARN (ResourceManager + NodeManager), HistoryServer, Spark Master e um Spark Worker, rede `bigdata`, **healthchecks** HTTP (`curl`) e **depends_on** com `service_healthy`. Configuração Hadoop em **`docker/hadoop.env`** com limites de memória **reduzidos** relativamente ao upstream para máquinas típicas de aluno.

## Motivação

Fechar a **T011** ([storyline](../../storyline/tasks/T011-compose-healthchecks.md)): compose reprodutível, documentação de portas/UIs e troubleshooting, sem segredos no Git (`.env` ignorado; `.env.example` como modelo).

## O que mudou

| Item | Detalhe |
|------|---------|
| Compose | Serviços com imagens pin conforme [docs/stack-apache.md](../stack-apache.md) |
| Git | [.gitignore](../../.gitignore) passa a ignorar `.env` |
| Storyline | T011 e tabela S01 marcados **Done** |

## Como verificar

```powershell
docker compose config
docker compose up -d
docker compose ps
```

Ver [docker/README.md](../../docker/README.md).

## Próximo passo

**T012:** montar/ingerir `Indian_Weather_Dataset.parquet` e smoke test de leitura no cluster.

## Riscos

Imagens **bde2020** antigas; primeira subida pode demorar ou falhar por RAM — ver secção Troubleshooting no `docker/README.md`.
