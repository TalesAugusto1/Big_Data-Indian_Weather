# T034 — Comparação de modelos e análise de erro

```yaml
id: T034
story: S03
milestone: M03
status: Todo
depends_on: [T031, T032, T033]
artifacts:
  - docs/comparacao_modelos.md ou tabela no notebook
```

## Objetivo

Consolidar **tabela comparativa** das três abordagens e uma **análise de erro**: matriz de confusão / curva ROC (classificação) ou resíduos vs predito (regressão), destacando onde cada modelo falha.

## Checklist

- [ ] Tabela única: modelo → hiperparâmetros-chave → métricas val/teste.
- [ ] Figura(s) de erro conforme tipo de tarefa.
- [ ] Parágrafo “qual modelo vence e por quê” + limitações.
- [ ] Riscos de overfitting e validação cruzada (se aplicável) mencionados.

## Evidence

- Copiar tabela final ou link para seção do notebook.

## Links

- Story: [../storys/S03-parte3-modelos-avaliacao.md](../storys/S03-parte3-modelos-avaliacao.md)
- Milestone: [../milestones/M03-modelagem-avaliacao.md](../milestones/M03-modelagem-avaliacao.md)
