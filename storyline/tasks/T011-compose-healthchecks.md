# T011 — Compose reproduzível e health checks

```yaml
id: T011
story: S01
milestone: M01
status: Todo
depends_on: [T010]
artifacts:
  - docker-compose.yml
  - README com comandos up/down/logs
```

## Objetivo

Ter arquivos **Docker Compose** (ou stack equivalente) que sobem o ambiente de forma **reprodutível**, com forma clara de checar **saúde** dos serviços.

## Checklist

- [ ] `docker compose up` (ou comando documentado) sobe sem passos manuais não documentados.
- [ ] Variáveis sensíveis apenas em `.env.example` (sem segredos reais no Git).
- [ ] Para cada serviço crítico: URL/porta ou comando `curl`/health documentado.
- [ ] Seção “Troubleshooting” com 2–3 falhas comuns (memória, portas).

## Evidence

- Trecho de log de subida bem-sucedida ou screenshot (opcional).
- Caminhos dos arquivos Compose no repositório.

## Links

- Story: [../storys/S01-parte1-ambiente-docker-apache.md](../storys/S01-parte1-ambiente-docker-apache.md)
- Milestone: [../milestones/M01-fundacao-big-data.md](../milestones/M01-fundacao-big-data.md)
