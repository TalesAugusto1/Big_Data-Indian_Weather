# Changelog: T012 — mount de dados + smoke Parquet no Spark

**Data:** 2026-04-21  
**Área:** Docker / M01 / Parte 1  
**Storyline:** [T012](../../storyline/tasks/T012-dataset-no-stack.md)

## Resumo

Montagem **read-only** de `./data` em **`/dataset`** nos serviços Spark e de `./scripts` em **`/opt/smoke`**, com script PySpark [`scripts/t012_smoke_parquet.py`](../../scripts/t012_smoke_parquet.py) para leitura mínima (schema + amostra; `count()` total opcional).

## Motivação

Fechar **T012** sem duplicar ficheiros gigantes no HDFS por defeito; manter opção documentada de `hdfs dfs -put` via `docker cp`.

## O que mudou

| Item | Detalhe |
|------|---------|
| [docker-compose.yml](../../docker-compose.yml) | Volumes nos serviços `spark-master` e `spark-worker` |
| [scripts/t012_smoke_parquet.py](../../scripts/t012_smoke_parquet.py) | Smoke PySpark |
| [docker/README.md](../../docker/README.md) | Secção **T012** com URIs e comandos |
| Storyline | T012 e DoD S01 atualizados |

## Como verificar

```powershell
docker compose up -d
docker compose exec spark-master /spark/bin/spark-submit /opt/smoke/t012_smoke_parquet.py
```

## Riscos

Requer PySpark na imagem `bde2020/spark`; se falhar, ver nota de caminho `spark-submit` no README.
