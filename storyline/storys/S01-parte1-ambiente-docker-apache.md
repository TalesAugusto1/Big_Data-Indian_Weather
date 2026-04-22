# S01 — Parte 1: Ambiente de Big Data (Docker + Apache)

```yaml
id: S01
milestone_primary: M01
status: Done
```

## Enunciado (referência)

> Parte 1: Construção de um Ambiente de Big Data — 1 ponto  
> Nesta parte do projeto, vocês irão construir um ambiente de big data com ecossitema Apache, utilizando o docker para simular um sistema de cluster de big data.

Fonte: [core.md](../../core.md).

## Problema / objetivo da story

Entregar um **ambiente reproduzível** que represente um **cluster Big Data** usando **Docker** e componentes do **ecossistema Apache**, preparado para processar o dataset do projeto.

## Critérios de aceite

- Uso de **Docker** para orquestrar os serviços.
- Stack alinhado ao pedido **Apache** (Hadoop/Spark/outros conforme curso); decisão **documentada**.
- Evidência de que o **dataset** pode ser lido a partir desse ambiente (smoke test).

## Dados de referência

- Parquet: `data/Indian_Weather_Dataset.parquet`
- CSV (arquivo): `data/archive/Indian_Weather_Dataset.csv`

## Definition of Done

- [x] Stack sobe com um comando documentado (`docker compose up` ou equivalente).
- [x] Documentação lista serviços, portas e como validar saúde.
- [x] Task **T012** em **Done** com evidência de leitura dos dados no ambiente.

## Índice de tasks

| Task ID | Título | Owner | Status |
|---------|--------|-------|--------|
| T010 | Escolha e documentação do stack Apache | | Done |
| T011 | Compose reproduzível e health checks | | Done |
| T012 | Dados montados/ingeridos + leitura mínima | | Done |

Arquivos: [../tasks/T010-docker-compose-stack.md](../tasks/T010-docker-compose-stack.md), [../tasks/T011-compose-healthchecks.md](../tasks/T011-compose-healthchecks.md), [../tasks/T012-dataset-no-stack.md](../tasks/T012-dataset-no-stack.md).

## Milestones relacionados

- Principal: [../milestones/M01-fundacao-big-data.md](../milestones/M01-fundacao-big-data.md)
