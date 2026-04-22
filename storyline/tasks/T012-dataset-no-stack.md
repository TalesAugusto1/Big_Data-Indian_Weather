# T012 — Ingestão ou mount + leitura mínima no stack

```yaml
id: T012
story: S01
milestone: M01
status: Done
depends_on: [T011]
artifacts:
  - scripts/t012_smoke_parquet.py
  - docker-compose.yml (volumes spark)
  - docker/README.md (secção T012)
```

## Objetivo

Colocar `data/Indian_Weather_Dataset.parquet` (ou cópia controlada) **acessível** dentro do ambiente clusterizado e executar uma **leitura mínima** (ex.: `spark.read.parquet`, `hdfs dfs -ls`, contagem de linhas).

## Checklist

- [x] Definir se os dados entram por **volume**, **copy-in** ou **HDFS put**.
- [x] Documentar caminho lógico usado pelos jobs (URI `hdfs://` ou `file://` conforme desenho).
- [x] Rodar job/comando de smoke e salvar saída (schema, `count`, amostra).
- [x] Anotar tempo aproximado ou limitações de recurso (RAM) se relevante.

## Decisão

- **Mount read-only:** `./data` → `/dataset` nos serviços **spark-master** e **spark-worker** ([docker-compose.yml](../../docker-compose.yml)).
- **Smoke:** PySpark em [scripts/t012_smoke_parquet.py](../../scripts/t012_smoke_parquet.py), URI por defeito `file:///dataset/Indian_Weather_Dataset.parquet` (override `T012_PARQUET_PATH`). `count()` completo só com `T012_FULL_COUNT=1`.

## Evidence

Comandos (colar saída real após executar no teu PC):

```powershell
docker compose up -d
docker compose exec spark-master /spark/bin/spark-submit /opt/smoke/t012_smoke_parquet.py
```

Documentação detalhada: [docker/README.md](../../docker/README.md) (secção **T012**).

## Links

- Story: [../storys/S01-parte1-ambiente-docker-apache.md](../storys/S01-parte1-ambiente-docker-apache.md)
- Milestone: [../milestones/M01-fundacao-big-data.md](../milestones/M01-fundacao-big-data.md)
