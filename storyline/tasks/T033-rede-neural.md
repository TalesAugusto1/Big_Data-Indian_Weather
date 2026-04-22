# T033 — Modelo de rede neural

```yaml
id: T033
story: S03
milestone: M03
status: Todo
depends_on: [T030]
artifacts:
  - notebook ou script da rede (Keras/PyTorch/sklearn MLP)
```

## Objetivo

Treinar uma **rede neural** para o mesmo alvo, com arquitetura e treino **documentados** (camadas, ativações, épocas, batch, early stopping se houver).

## Checklist

- [ ] Diagrama ou lista de camadas e unidades.
- [ ] Função de perda alinhada à tarefa.
- [ ] Registrar tempo aproximado de treino e hardware.
- [ ] Métricas no val/teste no protocolo de **T030**.

## Evidence

- Curva de loss opcional; métricas finais obrigatórias.

## Links

- Story: [../storys/S03-parte3-modelos-avaliacao.md](../storys/S03-parte3-modelos-avaliacao.md)
- Milestone: [../milestones/M03-modelagem-avaliacao.md](../milestones/M03-modelagem-avaliacao.md)
