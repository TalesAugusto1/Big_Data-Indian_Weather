# Desequilíbrio de classes — `rain_label` (M02 / T023)

## Objetivo

Documentar a **distribuição do alvo** `rain_label` (classificação binária, conforme [T020](../organization/evidencias/aprovacao.md)) e a **estratégia** para lidar com o desequilíbrio durante o treino, **sem** usar pandas nem scikit-learn na preparação descrita aqui (alinhado à [especificação de pré-processamento](preprocessamento.md)).

## Distribuição empírica

Valores obtidos com [`scripts/rain_label_counts.py`](../scripts/rain_label_counts.py) sobre `data/Indian_Weather_Dataset.parquet` (reexecutar o script se o dataset mudar):

### Frequências de `rain_label` (`data/Indian_Weather_Dataset.parquet`)

| classe | contagem | % do total |
|--------|----------|------------|
| 0 | 42,029,919 | 91.2065 |
| 1 | 4,052,241 | 8.7935 |

**Total (soma das classes na contagem):** 46,082,160  
**Linhas lidas na coluna:** 46,082,160

### Interpretação (PT-BR)

- A classe **0** (sem chuva / rótulo negativo, conforme convenção do dataset) é **majoritária** (~**91,2%** das linhas).
- A classe **1** é **minoritária** (~**8,8%**).
- Razão aproximada **majoritária : minoritária** ≈ **10,4 : 1** (42 029 919 / 4 052 241). Há **desequilíbrio forte**; métricas como acurácia “sempre 0” seriam enganosas — priorizar **F1 macro**, **recall da classe 1** e/ou **PR-AUC** na validação (já alinhado à T020).

## Estratégia escolhida (treino / Parte 3)

1. **Pesos de classe no treino (principal)**  
   Na modelagem em **Apache Spark** (Parte 3), usar **pesos por instância** ou equivalente na API do estimador escolhido, de forma que exemplos da classe **1** contribuam mais na função de perda do que os da classe **0**.  
   - Exemplo de intenção: peso proporcional ao inverso da frequência global no **treino** (calculado **após** o split temporal — só no conjunto treino, para não vazar contagens do val/teste).  
   - Parâmetros exatos (vetor de pesos ou `weightCol`) ficam definidos no notebook/código da Parte 3, mas a **regra** é: **nunca** ajustar pesos usando estatísticas do conjunto de **teste**.

2. **Threshold em probabilidade (secundário)**  
   Depois de obter probabilidades da classe positiva no conjunto de **validação**, ajustar o **limiar** (ex.: não usar 0,5 fixo) para equilibrar precisão/recall na classe 1, **reportando** o limiar escolhido e a métrica alvo.

3. **Resampling agressivo (opcional, não obrigatório)**  
   *Undersampling* da classe 0 ou *oversampling* da classe 1 **só no treino** pode ser experimentado se o Spark estiver limitado com pesos; documentar custo (perda de dados ou duplicação) na Parte 3. **Não** é requisito da T023 aplicar já no Parquet em disco.

## O que não faremos (e porquê)

- **Target encoding** da classe em features categóricas **como única** forma de “balancear” — alto risco de **leakage** se não for feito com CV estrita só no treino.  
- **Ajustar pesos ou amostragem com base no conjunto de teste** — invalida a avaliação.

## Ligações

- [preprocessamento.md](preprocessamento.md) (T022)  
- [scripts/profile_parquet.md](../scripts/profile_parquet.md) (perfil geral)  
- [scripts/split_temporal.md](../scripts/split_temporal.md) (T021)  
- Tarefa: [storyline/tasks/T023-desequilibrio-classes.md](../storyline/tasks/T023-desequilibrio-classes.md)
