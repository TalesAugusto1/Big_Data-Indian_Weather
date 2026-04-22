# `t012_smoke_parquet.py` — Smoke de leitura Parquet no Spark (T012)

## Objetivo

Validar que um ficheiro **Parquet** é legível pelo **Spark** (PySpark) dentro do ambiente do laboratório: imprime **esquema**, **uma linha** de amostra e `limit(1).count()` (evita `count()` global em ficheiros enormes, salvo pedido explícito).

## Onde corre

**Dentro** do contentor **`spark-master`** (ou worker, se preferir), normalmente via:

```powershell
docker compose exec spark-master /spark/bin/spark-submit /opt/smoke/t012_smoke_parquet.py
```

O script no repositório está montado em **`/opt/smoke/`**; o ficheiro Parquet do host está em **`/dataset/`** (bind mount de `./data`). Ver [`docker-compose.yml`](../docker-compose.yml) e [docker/README.md](../docker/README.md) (secção **T012**).

**Não** é necessário correr este script no host com `python` — no host normalmente não há PySpark configurado para o cluster; o fluxo oficial é `spark-submit` no contentor.

## Variáveis de ambiente

| Variável | Significado |
|----------|-------------|
| `T012_PARQUET_PATH` | Caminho **absoluto dentro do contentor** do ficheiro Parquet. Por defeito: `/dataset/Indian_Weather_Dataset.parquet`. Exemplo para ficheiro em subpasta: `/dataset/archive/Indian_Weather_Dataset.parquet`. |
| `T012_FULL_COUNT` | Se for exatamente `1`, após a amostra executa também `df.count()` sobre **todo** o dataset (varredura completa — **lenta** em dados muito grandes). |

### Exemplos com `docker compose exec`

Caminho por defeito (ficheiro em `data/Indian_Weather_Dataset.parquet` no host):

```powershell
docker compose exec spark-master /spark/bin/spark-submit /opt/smoke/t012_smoke_parquet.py
```

Parquet em `data/archive/`:

```powershell
docker compose exec -e T012_PARQUET_PATH=/dataset/archive/Indian_Weather_Dataset.parquet spark-master /spark/bin/spark-submit /opt/smoke/t012_smoke_parquet.py
```

Contagem total (opcional):

```powershell
docker compose exec -e T012_FULL_COUNT=1 spark-master /spark/bin/spark-submit /opt/smoke/t012_smoke_parquet.py
```

## Configuração Spark no script

- `SparkSession` com `appName("T012_smoke_parquet")`.
- `master("local[1]")` — um executor local **dentro** do JVM do `spark-submit` (smoke simples; não submete job ao cluster standalone como aplicação distribuída).
- Nível de log do Spark: `WARN`.

## Saída esperada

- Blocos `=== Esquema ===`, `=== Amostra (1 linha) ===`, `=== limit(1).count() === 1`.
- Se `T012_FULL_COUNT=1`, também `=== count() completo === <N>`.
- Linha final: `Smoke T012: OK`.
- Código de saída `0` em sucesso; `1` se o ficheiro não existir ou PySpark indisponível.

## Erros frequentes

| Mensagem | O que fazer |
|----------|-------------|
| `ERRO: Parquet não encontrado` | Confirmar que `./data` existe no host, que o Parquet está no sítio certo e que `T012_PARQUET_PATH` aponta para `/dataset/...` coerente com o mount. |
| `ERRO: PySpark indisponível` | Imagem ou `PYTHONPATH` sem PySpark; verificar caminho de `spark-submit` (`/spark/bin` vs `/opt/spark/bin`) e documentação da imagem `bde2020/spark-master`. |

## Leitura a partir do HDFS (opcional)

Se copiar o Parquet para o HDFS (ver guia em `docker/README.md`), defina `T012_PARQUET_PATH` para uma URI `hdfs://namenode:9000/...`.

## Ver também

- [docker/README.md](../docker/README.md) (secção **T012**)
- [Guia stack e dados](../docs/guides/stack-completo-e-dados.md)
- [Changelog T012](../docs/changelog/2026-04-21-t012-dataset-smoke.md)
- [Índice dos scripts](README.md)
