# M03 / T032: Regressão Linear com Regularização Ridge

**Resumo:** Treinamento do modelo paramétrico base (`LinearRegression`) para prever a variável contínua `temperature_C`, estabelecendo o primeiro passo da modelagem preditiva avançada.

## Motivação
Validar o comportamento das variáveis meteorológicas em um modelo paramétrico clássico de regressão linear. A aplicação da regularização L2 (Ridge) associada ao escalonamento (`StandardScaler`) garantiu a mitigação de multicolinearidade e overfitting em um volume expressivo de dados (46M+ registros).

## O que mudou
- **Pipeline:** Implementação do fluxo `VectorAssembler` → `StandardScaler` → `LinearRegression`.
- **Hiperparâmetros:** Solver configurado como `auto`, aplicação de penalidade Ridge (`elasticNetParam=0.0` e `regParam=0.1`).
- **Protocolo de Avaliação:** Manutenção do split 70/30 (Seed 42) definido na T030, focado em métricas de erro contínuo.

## Como verificar
Executar o notebook `notebooks/linear_regression.ipynb` com o dataset.