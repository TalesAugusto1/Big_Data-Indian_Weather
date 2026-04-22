# T012 — Ingestão ou mount + leitura mínima no stack

```yaml
id: T012
story: S01
milestone: M01
status: Todo
depends_on: [T011]
artifacts:
  - script ou notebook de smoke test
  - caminho HDFS/volume documentado
```

## Objetivo

Colocar `data/Indian_Weather_Dataset.parquet` (ou cópia controlada) **acessível** dentro do ambiente clusterizado e executar uma **leitura mínima** (ex.: `spark.read.parquet`, `hdfs dfs -ls`, contagem de linhas).

## Checklist

- [ ] Definir se os dados entram por **volume**, **copy-in** ou **HDFS put**.
- [ ] Documentar caminho lógico usado pelos jobs (URI `hdfs://` ou `file://` conforme desenho).
- [ ] Rodar job/comando de smoke e salvar saída (schema, `count`, amostra).
- [ ] Anotar tempo aproximado ou limitações de recurso (RAM) se relevante.

## Evidence

- Comando exato e trecho da saída (pode colar no próprio arquivo sob “Evidence”).

## Links

- Story: [../storys/S01-parte1-ambiente-docker-apache.md](../storys/S01-parte1-ambiente-docker-apache.md)
- Milestone: [../milestones/M01-fundacao-big-data.md](../milestones/M01-fundacao-big-data.md)
