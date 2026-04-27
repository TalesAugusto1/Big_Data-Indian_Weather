# Protocolo de Avaliação e Baseline (T030)

## 1. Definição do Problema e Métricas
Com base nas definições da tarefa T020, o projeto consiste em um problema de **Classificação**, tendo como variável alvo a coluna `rain_label`. 

**Métrica Principal:** F1-Score (macro).

A escolha do F1-Score foi feita pois o dataset, apresenta um grande desbalanceamento de classes, com isso a métrica de acurácia pode apresentar erros (enviesado). Utilizando o F1-Score podemos ter uma melhor precisão na avaliação final.

## 2. Protocolo de Divisão (Split)
Para garantir a reprodutibilidade e que todos os modelos da Fase 3 sejam comparáveis, o seguinte protocolo está congelado:
* **Proporção:** 70% Treino / 30% Teste.
* **Seed Global:** `42`.
* **Caminho dos Dados:** `data/Indian_Weather_Dataset.parquet`.

## 3. Baseline
Foi estabelecido um baseline não-inteligente (majority class) para servir como limite inferior.

**Regra do Baseline:** (Classe 0 - Sem Chuva)- Distribuição de Treino observada: 29.4M (Classe 0) e 2.8M (Classe 1).

### Resultados do Baseline (Conjunto de Teste):
* **F1-Score (macro):** 0.9540
