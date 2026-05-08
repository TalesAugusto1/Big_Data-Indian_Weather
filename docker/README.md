# Docker — stack Hadoop + Spark (M01)

Este diretório contém **`hadoop.env`** (configuração Hadoop/YARN/MapReduce) usado pelo [`docker-compose.yml`](../docker-compose.yml) na raiz do repositório.

**Leia primeiro [hadoop.env](hadoop.env)** — está documentado em português: convenção `CORE_CONF_*` / `HDFS_CONF_*` / `YARN_CONF_*` / `MAPRED_CONF_*`, o significado de `___` nos nomes, ligação aos serviços do Compose e um guia rápido para afinar memória.

Arquitetura e pins de imagem: [../docs/stack-apache.md](../docs/stack-apache.md).

Guia operacional aprofundado (clone → dados → smoke → HDFS opcional): [../docs/guides/stack-completo-e-dados.md](../docs/guides/stack-completo-e-dados.md).

## Pré-requisitos

- Docker Engine + **Docker Compose v2** (`docker compose`).
- **RAM** recomendada para Docker: **8 GB ou mais** (WSL2 / Docker Desktop). O `hadoop.env` foi afinado para um host com **~32 GB RAM / 16 threads** (ver bloco “Perfil da máquina” no topo desse ficheiro); noutro PC, baixe os MB do NodeManager e dos `mapreduce_*`.
- Portas **livres** no host (ver tabela abaixo).

## Arranque

Na raiz do repositório:

```powershell
copy .env.example .env
docker compose pull
docker compose up -d
docker compose ps
```

Ver estado de saúde:

```powershell
docker compose ps
```

Logs (exemplo):

```powershell
docker compose logs -f namenode
docker compose logs -f resourcemanager
docker compose logs -f spark-master
```

Parar e remover containers (mantém volumes HDFS):

```powershell
docker compose down
```

Parar e **apagar** volumes nomeados (apaga dados HDFS locais):

```powershell
docker compose down -v
```

## UIs e health checks

Os `healthcheck` do Compose usam **HTTP** nos endpoints locais do container (`curl`). Quando `docker compose ps` mostrar **healthy**, o serviço está pronto para o nível definido no check.

| Serviço | URL no host (padrão) | Notas |
|---------|----------------------|--------|
| HDFS NameNode | http://localhost:9870 | UI; RPC `9000` mapeado para HDFS |
| HDFS DataNode | http://localhost:9864 | UI |
| YARN ResourceManager | http://localhost:8088 | UI; API `ws/v1/cluster/info` usada no healthcheck |
| YARN NodeManager | http://localhost:8042 | UI; healthcheck na raiz HTTP |
| MapReduce History Server | http://localhost:8188 | Timeline / histórico |
| Spark Master | http://localhost:8080 | UI; porta **7077** Spark |
| Spark Worker | http://localhost:8081 | UI |
| Jupyter (PySpark) | http://localhost:8888 | Notebook no contentor `spark-notebook`; repo em `/home/jovyan/work`, dados em `/dataset`. Por defeito **`SPARK_MASTER=local[4]`** e **`SPARK_DRIVER_MEMORY=3g`** (e limites associados; ver `.env.example`). Para `spark://spark-master:7077`, ver `JUPYTER_SPARK_MASTER`. Porta: `JUPYTER_PORT` no `.env`. |

Portas podem ser alteradas via variáveis no `.env` (ver [.env.example](../.env.example)).

## Validação rápida (opcional)

```powershell
docker compose config
curl -fsS http://localhost:9870/ | Out-Null
curl -fsS http://localhost:8088/ws/v1/cluster/info | Out-Null
curl -fsS http://localhost:8080/ | Out-Null
```

## Troubleshooting

1. **`dependency failed to start: container namenode is unhealthy`**  
   Primeira subida pode demorar (formatação HDFS). Aumente `start_period` / `retries` no compose ou aguarde e execute `docker compose up -d` novamente. Verifique RAM atribuída ao Docker.

2. **`port is already allocated`**  
   Altere as portas publicadas no `.env` (variáveis listadas em `.env.example`) ou pare o processo que ocupa a porta.

3. **`curl` not found** nos healthchecks (imagem sem `curl`)  
   As imagens `bde2020` costumam incluir `curl`. Se falhar, substitua o `healthcheck` por `wget` ou por verificação TCP (`/dev/tcp`) e documente a alteração.

4. **NodeManager ou RM reiniciam em loop**  
   Memória insuficiente: reduza ainda mais `YARN_CONF_yarn_nodemanager_resource_memory___mb` e limites `MAPRED_CONF_*` em `docker/hadoop.env`, depois `docker compose down -v` e suba de novo (apaga dados HDFS).

5. **`Lost executor … Remote RPC client disassociated. Likely due to containers exceeding thresholds`** (logs do `spark-notebook` ou do worker)  
   Os JVMs dos **executors** no `spark-worker` foram mortos (quase sempre **OOM** do Docker). Com **um só worker**, muitos executores com **2g** cada esgotam a RAM. O serviço `notebook` no `docker-compose.yml` define `SPARK_EXECUTOR_MEMORY`, `SPARK_EXECUTOR_CORES` e `SPARK_CORES_MAX` (sobrescrevíveis no `.env`); o `decision_tree.ipynb` lê-as no modo cluster. Aumente a RAM do Docker Desktop ou baixe esses valores.

6. **Py4J / `show()` a falhar no Jupyter com `spark://spark-master:7077`**  
   Por defeito o Compose passa **`SPARK_MASTER=local[4]`** ao contentor `notebook` (Spark só no Jupyter, sem executors no worker). Se tiver definido **`JUPYTER_SPARK_MASTER=spark://spark-master:7077`** e continuar a perder executors, aumente RAM ao Docker ou volte ao defeito `local[4]` (apague a variável do `.env` e `docker compose up -d --force-recreate notebook`).

7. **`Connection reset by peer` / Py4J em `fit()` no `decision_tree.ipynb`**  
   Com **`local[4]`**, o **driver** partilha a JVM com os “executors” locais; pedir **8g** de heap num contentor com **2–4 GiB** de limite mata o processo Java durante o treino. O Compose define por defeito **`SPARK_DRIVER_MEMORY=3g`**, **`SPARK_DRIVER_MAX_RESULT_SIZE=768m`**, **`SPARK_DEFAULT_PARALLELISM=4`** e **`SPARK_SQL_SHUFFLE_PARTITIONS=8`** (sobrescrevíveis no `.env`). Depois de alterar: `docker compose up -d --force-recreate notebook`, **reiniciar o kernel** e voltar a correr desde a primeira célula.

8. **Mesmo erro no `train_vec.limit(3).show()` (preview)**  
   **`randomSplit`** força uma passagem por **todas** as linhas de `model_df`; com **`persist(MEMORY_AND_DISK)`** no dataset completo o driver facilmente rebenta. O notebook passou a usar **`DISK_ONLY`** e o Compose define **`DTR_NOTEBOOK_MAX_ROWS`** (por defeito **400000**) para limitar o volume antes do split. Para o dataset inteiro no Docker, aumente RAM e/ou suba o limite no `.env`; no host, `MAX_ROWS` no notebook continua a mandar.

## T012 — Dados montados + smoke Parquet (Spark)

### Desenho

- O host expõe o diretório **`./data`** como **`/dataset`** (read-only) nos containers **`spark-master`** e **`spark-worker`**.
- Os scripts do repositório ficam em **`/opt/smoke`** (read-only), incluindo [`../scripts/t012_smoke_parquet.py`](../scripts/t012_smoke_parquet.py).
- **URI por defeito no smoke:** `file:///dataset/Indian_Weather_Dataset.parquet`  
  Alternativa comum: `file:///dataset/archive/Indian_Weather_Dataset.parquet` (definir `T012_PARQUET_PATH`).

No **Docker Desktop (Windows)**, o caminho `./data` é relativo à pasta onde está o `docker-compose.yml`. Crie a pasta se ainda não existir:

```powershell
New-Item -ItemType Directory -Force -Path .\data | Out-Null
```

### Pré-requisitos

- Stack no ar: `docker compose up -d` e serviços Spark **healthy**.
- Ficheiro Parquet presente no host, por exemplo:
  - `data/Indian_Weather_Dataset.parquet`, ou
  - `data/archive/Indian_Weather_Dataset.parquet` (ajuste `T012_PARQUET_PATH` abaixo).

### Smoke test (leitura mínima)

Por defeito o script imprime **schema**, **1 linha** e `limit(1).count()` (evita `count()` completo em ficheiros gigantes). Para `count()` total (varre tudo — pode demorar):

```powershell
docker compose exec -e T012_FULL_COUNT=1 spark-master /spark/bin/spark-submit /opt/smoke/t012_smoke_parquet.py
```

Caminho alternativo do ficheiro:

```powershell
docker compose exec -e T012_PARQUET_PATH=/dataset/archive/Indian_Weather_Dataset.parquet spark-master /spark/bin/spark-submit /opt/smoke/t012_smoke_parquet.py
```

Comando padrão:

```powershell
docker compose exec spark-master /spark/bin/spark-submit /opt/smoke/t012_smoke_parquet.py
```

Se `/spark/bin/spark-submit` não existir na imagem, experimente `/opt/spark/bin/spark-submit` (verificar com `docker compose exec spark-master ls /spark/bin`).

### Opcional — copiar para o HDFS (narrativa cluster)

O container **namenode** não monta `./data` por defeito. Copie do host para o NameNode e depois para o HDFS:

```powershell
docker cp .\data\Indian_Weather_Dataset.parquet namenode:/tmp/Indian_Weather_Dataset.parquet
docker compose exec namenode hdfs dfs -mkdir -p /user/lab
docker compose exec namenode hdfs dfs -put -f /tmp/Indian_Weather_Dataset.parquet /user/lab/
docker compose exec namenode hdfs dfs -ls /user/lab
```

Leitura via Spark com URI **`hdfs://namenode:9000/user/lab/Indian_Weather_Dataset.parquet`** (definir `T012_PARQUET_PATH` em `docker compose exec -e ...`).
