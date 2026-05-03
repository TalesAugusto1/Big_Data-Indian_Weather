# Changelog — M03 / T031: robustez do `decision_tree.ipynb` (Spark no host e deps)

**Data:** 2026-05-02

## Resumo

Endurecimento do notebook **`notebooks/decision_tree.ipynb`** para arranque fiável de **PySpark** no Windows / kernel Jupyter (JAVA_HOME, `SPARK_MASTER`, gateway Py4J após crash, memória do driver) e ajuste de preparação de dados para reduzir **OOM** na fase de treino e **antes** do treino (*preview* após `randomSplit`). No **Docker Compose**, o serviço `notebook` recebe por defeito limites de heap/partições e **`DTR_NOTEBOOK_MAX_ROWS`** para não varrer o Parquet inteiro num contentor com pouca RAM. **`requirements.txt`**: `setuptools>=69` para compatibilidade de `distutils` com **Python 3.12+** (necessário a `pyspark.ml`). Comentários no **`docker/hadoop.env`** ligam RAM YARN vs Spark/Jupyter.

## Motivação

- Falhas **`ModuleNotFoundError: distutils`** com Python recente sem `setuptools`.
- **`JAVA_GATEWAY_EXITED`** / master vazio quando `SPARK_MASTER` existia mas estava `""`.
- **`ConnectionRefusedError`** após **OOM** da JVM: estado Py4J zumbi entre reexecuções da primeira célula.
- **`OutOfMemoryError: Java heap space`** em `fit()` com dataset completo em modo local.
- **`Connection reset` / Py4J** em `train_vec.limit(3).show()`: `randomSplit` percorre **todas** as linhas; `persist(MEMORY_AND_DISK)` no `model_df` completo esgotava o driver em **`local[4]`** com heap ~3g.
- Documentação da equipa: fluxo preferencial via **Jupyter no Docker** (README + SKILL); o notebook continua executável no host com estas proteções.

## O que mudou

| Caminho | Alteração |
|---------|-----------|
| `requirements.txt` | `setuptools>=69.0.0` para expor o shim de `distutils` usado por PySpark ML em Python 3.12+. |
| `notebooks/decision_tree.ipynb` | `JAVA_HOME` automático (Microsoft OpenJDK em `Program Files`, fallback `which java`) quando o kernel não herda variáveis do shell. |
| `notebooks/decision_tree.ipynb` | Normalização de `SPARK_MASTER` (vazio → `local[4]`); se `spark://…` não resolver por DNS no host, aviso e fallback para `local[4]`. |
| `notebooks/decision_tree.ipynb` | `_reset_spark_if_stale()` para limpar `SparkSession` / `SparkContext` / gateway antes de `getOrCreate()` após falhas da JVM. |
| `notebooks/decision_tree.ipynb` | Modo **local**: `spark.driver.memory` via **`SPARK_DRIVER_MEMORY`** ou defeito **8g** no host; `maxResultSize`, `spark.sql.shuffle.partitions` e `spark.default.parallelism` lidos de env quando definidos (Compose Jupyter define valores seguros). |
| `docker-compose.yml` (serviço `notebook`) | **`SPARK_DRIVER_MEMORY=3g`**, **`SPARK_DRIVER_MAX_RESULT_SIZE=768m`**, **`SPARK_DEFAULT_PARALLELISM=4`**, **`SPARK_SQL_SHUFFLE_PARTITIONS=8`**, **`DTR_NOTEBOOK_MAX_ROWS=400000`** por defeito (evita **Connection reset** no driver; `randomSplit` varre todo `model_df`). |
| `notebooks/decision_tree.ipynb` | **`DTR_NOTEBOOK_MAX_ROWS`** na 1.ª célula; **`persist(DISK_ONLY)`** em vez de `MEMORY_AND_DISK` no `model_df`. |
| `.env.example` / `docker/README.md` / `README.md` | Variáveis (`SPARK_DRIVER_*`, `DTR_NOTEBOOK_MAX_ROWS`, …); troubleshooting **#7** (heap driver / `fit`) e **#8** (`randomSplit` + preview / cache em disco). |
| `docker/hadoop.env` | Bloco final de comentários: RAM YARN vs executors Spark no worker vs modo **`local[4]`** do Jupyter; pointer para `docker/README.md`. |
| `notebooks/decision_tree.ipynb` | Remoção do bloco longo de descoberta Java (`java -version` / scan manual); preparação de dados: **`coalesce(8)`** em vez de **`repartition(16)`** para evitar shuffle desnecessário antes do ML. |

## Como verificar

1. **`pip install -r requirements.txt`** num venv (ex.: 3.12–3.14) e `python -c "from pyspark.ml.feature import VectorAssembler"` sem erro.
2. **Host:** abrir `notebooks/decision_tree.ipynb`, reiniciar kernel, correr a primeira célula com e sem `JAVA_HOME` no ambiente do kernel.
3. **Docker (recomendado para alinhamento ao cluster):** `docker compose up -d`, Jupyter em **http://localhost:8888**, executar o notebook no contentor (ver [README.md](../../README.md#notebooks-jupyter-docker)). Após alterar env do contentor: `docker compose up -d --force-recreate notebook`, reiniciar kernel, correr desde a 1.ª célula.

## Riscos / limites

- No **host** sem variáveis, o notebook ainda pode pedir **8g** ao driver; definir `SPARK_DRIVER_MEMORY` ou usar amostragem (`SAMPLE_FRACTION` / `MAX_ROWS`).
- **`DTR_NOTEBOOK_MAX_ROWS`** (Compose) limita linhas para notebooks em Docker; dataset completo no contentor exige mais RAM Docker e/ou `MAX_ROWS=None` com cuidado.
- Fallback **`local[4]`** quando `spark-master` não resolve no host **não** substitui a execução intencional no cluster: para evidência de cluster, usar o Jupyter do Compose.

## Relacionado

- Entrada anterior T031 / EDA: [2026-04-30-m03-t031-decision-tree-eda-regressao.md](2026-04-30-m03-t031-decision-tree-eda-regressao.md).
- Fluxo Jupyter Docker: [README.md](../../README.md#notebooks-jupyter-docker), [.cursor/skills/milestone-branch-workflow/SKILL.md](../../.cursor/skills/milestone-branch-workflow/SKILL.md).
