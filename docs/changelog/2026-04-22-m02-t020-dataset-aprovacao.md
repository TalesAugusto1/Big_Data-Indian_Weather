# Changelog: M02 / T020 — Dataset aprovado, alvo e evidência

**Data:** 2026-04-22  
**Área:** Storyline M02 / S02 / Parte 2  
**Storyline:** [T020](../../storyline/tasks/T020-dataset-aprovacao-alvo.md)

## Resumo

Registo formal do **Indian Weather** como dataset da disciplina, definição do **alvo** (`rain_label`, classificação), **métrica principal planeada** (F1 macro; AUROC como secundária quando aplicável), caminhos de ficheiros e nota sobre o critério **> 1 GB** (CSV fonte + Parquet / aprovação docente). Evidência de **aprovação do professor** com data e meio genérico.

## Motivação

Fechar **T020** como pré-requisito de **T021** (split temporal) e restantes tarefas M02, com documentação auditável no repositório.

## O que mudou

| Item | Detalhe |
|------|---------|
| [organization/evidencias/aprovacao.md](../../organization/evidencias/aprovacao.md) | Evidência única: dataset, tamanhos, alvo, métricas, aprovação |
| [storyline/tasks/T020-dataset-aprovacao-alvo.md](../../storyline/tasks/T020-dataset-aprovacao-alvo.md) | `status: Done`, checklist, Evidence |
| [storyline/storys/S02-parte2-eda-preprocessamento.md](../../storyline/storys/S02-parte2-eda-preprocessamento.md) | S02 `Doing`, T020 na tabela **Done**, DoD T020 marcado |
| [storyline/milestones/M02-dados-aprovados-eda.md](../../storyline/milestones/M02-dados-aprovados-eda.md) | Marco M02 `Doing` |

## Como verificar

1. Ler [organization/evidencias/aprovacao.md](../../organization/evidencias/aprovacao.md).
2. Confirmar no GitHub que `T020` aparece como **Done** no ficheiro da task e na tabela da S02.

## Dependências / follow-ups

- **T021:** implementar split temporal reproduzível e documentação anti-leakage.
- Opcional: atualizar tamanhos em bytes no `aprovacao.md` com saída real de `Get-Item` quando os ficheiros estiverem presentes na máquina de cada membro.
