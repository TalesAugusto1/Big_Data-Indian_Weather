# T011 — Compose reproduzível e health checks

```yaml
id: T011
story: S01
milestone: M01
status: Done
depends_on: [T010]
artifacts:
  - docker-compose.yml
  - docker/hadoop.env
  - .env.example
  - docker/README.md
```

## Objetivo

Ter arquivos **Docker Compose** (ou stack equivalente) que sobem o ambiente de forma **reprodutível**, com forma clara de checar **saúde** dos serviços.

## Checklist

- [x] `docker compose up` (ou comando documentado) sobe sem passos manuais não documentados.
- [x] Variáveis sensíveis apenas em `.env.example` (sem segredos reais no Git); `.env` ignorado no Git.
- [x] Para cada serviço crítico: URL/porta ou comando `curl`/health documentado.
- [x] Seção “Troubleshooting” com 2–3 falhas comuns (memória, portas).

## Evidence

- Compose na raiz: [docker-compose.yml](../../docker-compose.yml)
- Config Hadoop: [docker/hadoop.env](../../docker/hadoop.env)
- Variáveis de exemplo: [.env.example](../../.env.example)
- Documentação: [docker/README.md](../../docker/README.md)
- Validação de sintaxe: `docker compose config` (executado com sucesso no ambiente de desenvolvimento).

## Links

- Story: [../storys/S01-parte1-ambiente-docker-apache.md](../storys/S01-parte1-ambiente-docker-apache.md)
- Milestone: [../milestones/M01-fundacao-big-data.md](../milestones/M01-fundacao-big-data.md)
