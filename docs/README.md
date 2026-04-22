# Índice da documentação

Comece aqui se for novo no repositório. A documentação do projeto está **em português** (este índice, `README.md` na raiz, guias em `docs/guides/`, `docs/stack-apache.md`, `docker/README.md`).

## Ler primeiro

| Documento | O que aprende |
|-----------|----------------|
| [../README.md](../README.md) | Início rápido: stack Docker, dados, venv Python, CSV→Parquet, ligações para guias |
| [guides/stack-completo-e-dados.md](guides/stack-completo-e-dados.md) | **Guia aprofundado**: arquitetura, portas, ficheiros de ambiente, ordem de arranque, smoke, HDFS opcional, resolução de problemas |
| [stack-apache.md](stack-apache.md) | Porquê este stack Apache/Hadoop/Spark (bde2020), pins de imagem, topologia |
| [../docker/README.md](../docker/README.md) | Comandos Docker Compose, tabela de UIs, smoke T012, troubleshooting |
| [../core.md](../core.md) | Rubrica da disciplina |
| [changelog/README.md](changelog/README.md) | Entradas de changelog por funcionalidade |

## Por tarefa (laboratório M01)

1. **Compreender a decisão de stack** → [stack-apache.md](stack-apache.md) (T010).
2. **Correr Hadoop + Spark no Docker** → [guides/stack-completo-e-dados.md](guides/stack-completo-e-dados.md) + [../docker/README.md](../docker/README.md) (T011–T012).
3. **Converter CSV para Parquet no host** → [../README.md](../README.md) (secção Python) e [changelog/2026-04-21-csv-to-parquet-streaming.md](changelog/2026-04-21-csv-to-parquet-streaming.md).

## Scripts (`scripts/`)

- [../scripts/README.md](../scripts/README.md) — índice e ligações a `csv_to_parquet.md` e `t012_smoke_parquet.md`.

## Acompanhamento do curso

- [../storyline/README.md](../storyline/README.md) — marcos, histórias, tarefas.
