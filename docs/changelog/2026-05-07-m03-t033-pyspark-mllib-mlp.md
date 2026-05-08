# Changelog: M03 — T033 rede neural PySpark (MLlib MLP + discretização)

**Área:** Storyline M03 / S03 / T033  
**Storyline:** [T033](../../storyline/tasks/T033-rede-neural.md)

## Resumo

Novo notebook **`notebooks/neural_network_pyspark_mllib.ipynb`**: treino de **`MultilayerPerceptronClassifier`** no mesmo protocolo que **`decision_tree.ipynb`** (Parquet, features numéricas, split 70/30, `seed=42`, métricas MAE/RMSE/R² no **teste**). Como o Spark MLlib não expõe MLP para regressão, o alvo **`temperature_C`** é discretizado com **`QuantileDiscretizer`** (fit apenas no treino); as predições multiclasse são mapeadas ao **ponto médio do bin** para reportar graus Celsius comparáveis ao T030.

## Motivação

Substituir o treino apenas em NumPy/PyArrow por uma evidência **PySpark** que aproveita o cluster Standalone/HDFS descrito no `docker-compose` quando `JUPYTER_SPARK_MASTER=spark://spark-master:7077`.

## O que mudou

| Caminho | Alteração |
|---------|-----------|
| `notebooks/neural_network_pyspark_mllib.ipynb` | SparkSession (mesmo padrão do DT), `QuantileDiscretizer`, `MultilayerPerceptronClassifier` (`layers`, `maxIter`, `blockSize`, `solver`), tempo/hardware, métricas + baseline, save opcional em `models/multilayer_perceptron_t033`, `spark.stop()` |
| `storyline/tasks/T033-rede-neural.md` | Evidência principal = notebook PySpark; NumPy mantido como referência histórica |

## Como correr / verificar

1. JDK 17+ (`JAVA_HOME`). Dataset em `data/Indian_Weather_Dataset.parquet` ou montagem `/dataset` no container Jupyter.
2. Abrir o notebook e executar todas as células (kernel PySpark do contentor `jupyter/pyspark-notebook:spark-3.2.1` recomendado).
3. Opcional: definir `JUPYTER_SPARK_MASTER` e memórias de executor no `.env` para usar workers.
4. A primeira célula de código prefixa `sys.path` com `SPARK_HOME/python` e o `py4j-*-src.zip` em `lib/`, para `jupyter nbconvert --execute` e outros processos sem o kernel Jupyter carregar `pyspark`/`py4j`.
5. Verificação: `docker compose exec -e DTR_NOTEBOOK_MAX_ROWS=15000 notebook bash -lc "cd /home/jovyan/work && jupyter nbconvert --to notebook --execute notebooks/neural_network_pyspark_mllib.ipynb --output /tmp/nn_exec_test.ipynb"` concluiu com sucesso (stack local em 2026-05-08).

## Dependências

- Stack Docker descrito em `docker-compose.yml` (Notebook + Spark Master/Worker + HDFS).

## Follow-ups

- Curva de loss por época não é exposta de forma trivial pelo `MultilayerPerceptronClassifier`; permanece opcional no checklist T033.
