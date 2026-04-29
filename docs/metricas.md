# Protocolo de Avaliação e Baseline (T030)

## 1. Definição do Problema e Métricas
O escopo foi atualizado de classificacao (`rain_label`) para **regressao**, com alvo na coluna `temperature_C`.

### Por que a mudanca foi necessaria

No formato de classificacao, o dataset ficou fortemente desbalanceado (muito mais casos de "sem chuva"). Para equilibrar, seria necessario um corte agressivo da classe majoritaria (undersampling) ou reamostragem artificial, o que:

- descartaria uma parte muito grande dos dados reais;
- reduziria diversidade temporal e meteorologica;
- aumentaria risco de vies no treino;
- poderia comprometer a generalizacao.

Com regressao em `temperature_C`, preservamos muito mais informacao do dataset e evitamos esse corte extremo.

**Metricas principais:** `MAE`, `RMSE` e `R2`.

## 2. Protocolo de Divisão (Split)
Para garantir a reprodutibilidade e que todos os modelos da Fase 3 sejam comparáveis, o seguinte protocolo está congelado:
* **Proporção:** 70% Treino / 30% Teste.
* **Seed Global:** `42`.
* **Caminho dos Dados:** `data/Indian_Weather_Dataset.parquet`.

## 3. Baseline
Foi estabelecido baseline de regressao para servir como limite inferior e referencia de comparacao entre modelos.

### Estrategias avaliadas

- `media_global`
- `media_por_hour`
- `media_por_month`
- `media_por_hour_month`

### Resultados do Baseline (Conjunto de Teste):
| Modelo | MAE | RMSE | R2 |
|--------|-----:|-----:|----:|
| `media_global` | 5.6717 | 7.5320 | -0.0000 |
| `media_por_hour` | 5.2105 | 6.8883 | 0.1636 |
| `media_por_month` | 4.8466 | 6.5393 | 0.2462 |
| `media_por_hour_month` | 4.1508 | 5.7196 | 0.4233 |

Leitura: `hour` e `month` carregam sinal preditivo relevante; por isso `media_por_hour_month` virou baseline minimo para os proximos modelos supervisionados.