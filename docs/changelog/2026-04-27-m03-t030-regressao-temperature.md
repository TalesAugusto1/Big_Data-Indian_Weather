# Changelog — M03 / T030: baseline de regressao em `temperature_C`

**Data:** 2026-04-27

## Resumo

Migracao do baseline de classificacao (`rain_label`) para **regressao** com alvo `temperature_C`, incluindo fallback local para PyArrow quando Spark falha no ambiente Windows, e ampliacao para baselines sazonais (`hour`, `month`, `hour+month`).

## Motivacao

Alinhar a tarefa T030 ao novo objetivo do projeto (previsao de temperatura), removendo dependencia de metricas de classificacao e estabelecendo um benchmark mais forte para os modelos da M03.

## O que mudou

| Caminho | Alteracao |
|---------|-----------|
| `notebooks/eda.ipynb` | EDA reorientada para regressao em `temperature_C` (distribuicao, sazonalidade por `hour`/`month`, relacoes com preditores e ranking numerico de correlacoes). |
| `scripts/calcula_base.py` | Troca de baseline de classe majoritaria para regressao constante (media), com metricas `MAE`, `RMSE`, `R2`. |
| `scripts/calcula_base.py` | Inclusao de fallback `PyArrow` para erro de Spark (`getSubject is not supported`) em execucao local. |
| `scripts/calcula_base.py` | Comparativo de 4 baselines: `media_global`, `media_por_hour`, `media_por_month`, `media_por_hour_month`. |

## Evidencia de resultado (execucao local)

Saida observada no fallback PyArrow:

- `media_global`: MAE `5.6717`, RMSE `7.5320`, R2 `-0.0000`
- `media_por_hour`: MAE `5.2105`, RMSE `6.8883`, R2 `0.1636`
- `media_por_month`: MAE `4.8466`, RMSE `6.5393`, R2 `0.2462`
- `media_por_hour_month`: MAE `4.1508`, RMSE `5.7196`, R2 `0.4233`

Interpretacao: `hour` e `month` capturam sinal sazonal relevante e elevam bastante o baseline da tarefa.

## Como verificar

1. Ativar o venv do projeto.
2. Garantir `data/Indian_Weather_Dataset.parquet` disponivel.
3. Executar:
   - `python scripts/calcula_base.py`
4. Confirmar impressao da tabela comparativa com as 4 estrategias de baseline.
5. (Opcional) Abrir `notebooks/eda.ipynb` e executar as celulas de correlacao/sazonalidade para validar a leitura exploratoria.

## Follow-up

- Usar `media_por_hour_month` como benchmark minimo para os modelos supervisionados da M03.
- Evoluir para modelos de regressao com features meteorologicas completas, mantendo avaliacao em `MAE`, `RMSE` e `R2`.
