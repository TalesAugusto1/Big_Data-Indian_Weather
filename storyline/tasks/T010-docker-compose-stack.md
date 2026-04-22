# T010 — Escolha e documentação do stack Apache

```yaml
id: T010
story: S01
milestone: M01
status: Done
depends_on: []
artifacts:
  - docs/stack-apache.md
```

## Objetivo

Definir quais componentes do **ecossistema Apache** entram no ambiente (ex.: HDFS, YARN, Spark — conforme orientação do professor) e **registrar versões e papéis** de cada serviço.

## Checklist

- [x] Listar requisitos mínimos do curso para “cluster simulado”.
- [x] Escolher imagens oficiais ou comunidade com versão fixa (pin).
- [x] Documentar topologia (quais containers, dependências entre si).
- [x] Registrar decisões rejeitadas em uma linha (opcional, mas útil).

## Evidence

- Documento: [docs/stack-apache.md](../../docs/stack-apache.md)
- Tabela **Serviço → imagem Docker (tag fixa) → papel → portas** incluída no doc; stack **bde2020** Hadoop `2.0.0-hadoop3.2.1-java8` + Spark `3.2.1-hadoop3.2`.
- Diagrama mermaid de topologia no mesmo arquivo.

## Links

- Story: [../storys/S01-parte1-ambiente-docker-apache.md](../storys/S01-parte1-ambiente-docker-apache.md)
- Milestone: [../milestones/M01-fundacao-big-data.md](../milestones/M01-fundacao-big-data.md)
