# T010 — Escolha e documentação do stack Apache

```yaml
id: T010
story: S01
milestone: M01
status: Todo
depends_on: []
artifacts:
  - docs/stack-apache.md   # criar quando existir; ou seção no README do docker/
```

## Objetivo

Definir quais componentes do **ecossistema Apache** entram no ambiente (ex.: HDFS, YARN, Spark — conforme orientação do professor) e **registrar versões e papéis** de cada serviço.

## Checklist

- [ ] Listar requisitos mínimos do curso para “cluster simulado”.
- [ ] Escolher imagens oficiais ou comunidade com versão fixa (pin).
- [ ] Documentar topologia (quais containers, dependências entre si).
- [ ] Registrar decisões rejeitadas em uma linha (opcional, mas útil).

## Evidence

- Link ou caminho do documento onde o stack está descrito.
- Tabela serviço → imagem → versão.

## Links

- Story: [../storys/S01-parte1-ambiente-docker-apache.md](../storys/S01-parte1-ambiente-docker-apache.md)
- Milestone: [../milestones/M01-fundacao-big-data.md](../milestones/M01-fundacao-big-data.md)
