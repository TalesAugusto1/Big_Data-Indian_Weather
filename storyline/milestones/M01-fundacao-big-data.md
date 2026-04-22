# M01 — Fundação Big Data

```yaml
id: M01
status: Todo
```

## Objetivo

Ter um **ambiente de Big Data com ecossistema Apache** simulado via **Docker**, com dados do Indian Weather **acessíveis** dentro do stack (leitura mínima comprovada).

## Datas-alvo (ajustar ao calendário do curso)

Referência de apresentações finais no enunciado: **11/05**, **13/05**, **25/05**, **27/05**. Definir internamente uma data-alvo para concluir M01 **antes** de avançar pesado em EDA/modelagem.

## Critérios de saída

- Componentes Apache escolhidos e **documentados** (versões, papéis).
- `docker compose` (ou equivalente) sobe o stack com passos reproduzíveis.
- **Smoke test**: job ou comando que lê o dataset (ex.: contagem de linhas / schema) a partir do ambiente clusterizado ou volume montado conforme a arquitetura escolhida.
- README ou doc do stack com portas, credenciais de dev, e troubleshooting mínimo.

## Storys ligadas

- [S01 — Parte 1: Ambiente Docker + Apache](../storys/S01-parte1-ambiente-docker-apache.md)

## Tasks ligadas

| ID | Título | Arquivo |
|----|--------|---------|
| T010 | Escolha do stack Apache | [../tasks/T010-docker-compose-stack.md](../tasks/T010-docker-compose-stack.md) |
| T011 | Compose reproduzível e health checks | [../tasks/T011-compose-healthchecks.md](../tasks/T011-compose-healthchecks.md) |
| T012 | Ingestão/mount + leitura mínima dos dados | [../tasks/T012-dataset-no-stack.md](../tasks/T012-dataset-no-stack.md) |
