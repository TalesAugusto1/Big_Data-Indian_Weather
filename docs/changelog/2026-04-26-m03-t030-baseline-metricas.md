# M03 / T030: Avaliação e Baseline

**Resumo:** Definição da métrica principal (F1-Score), protocolo de corte 70/30 e extração do baseline de classe majoritária.

## Motivação
Estabelecer uma base de performance e garantir que todos os modelos da Milestone M3 utilizem a mesma base de comparação e avaliação.

## O que mudou
- **Docs:** Criação de `docs/metricas.md` com as definições de F1-Score Macro.
- **Scripts:** Adicionado `scripts/calcula_base.py` para execução via Spark.
- **Resultados:** F1-Score do baseline registrado como 0.9540 (Classe 0 predominante).

## Como verificar
1. Garantir que o Docker está rodando com recursos de memória ajustados (>12GB).
2. Executar: 
   `docker compose exec spark-master /spark/bin/spark-submit /opt/smoke/calcula_base.py`

## Follow-up
- A T031 (Árvore de Decisão) deve obrigatoriamente usar o corte e métrica definidos nesta tarefa.
