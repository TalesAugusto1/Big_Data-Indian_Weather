# Aprovação do dataset e definição do problema (M02 / T020)

## Dataset

- **Nome:** Indian Weather (conjunto meteorológico agregado por local e tempo, estilo Kaggle / fonte académica equivalente).
- **Ficheiro analítico (Parquet):** `data/Indian_Weather_Dataset.parquet`  
  - *Nota:* a pasta `data/` não é versionada no Git; o ficheiro existe no ambiente local de laboratório e no stack Docker (mount `.\data` → `/dataset`).
- **Referência de tamanho (verificação local, smoke Spark / HDFS):** ficheiro Parquet com **~844 MB** (~844 058 318 bytes) numa cópia verificada no laboratório (ex.: após `hdfs dfs -put` para `/user/lab/`).

## Requisito “> 1 GB” (enunciado Parte 2)

O Parquet comprimido pode ficar **abaixo de 1 GB** e ainda assim representar o mesmo conjunto Indian Weather. O **volume bruto** do projeto cumpre o critério de **> 1 GB** através do **ficheiro CSV fonte** em `data/archive/Indian_Weather_Dataset.csv` (típico do dataset Indian Weather em Kaggle: ordem de **vários gigabytes** em disco antes da conversão para Parquet).  
**Confirmação do docente:** o conjunto Indian Weather foi **aprovado** para uso na disciplina, incluindo aceitação do critério de volume no conjunto completo (CSV + Parquet / pipeline de dados).

Para auditoria local, pode repetir no PowerShell (ajuste o caminho se o CSV estiver outro sítio):

```powershell
Get-Item .\data\archive\Indian_Weather_Dataset.csv, .\data\Indian_Weather_Dataset.parquet |
  Select-Object Name, @{N='SizeGB';E={[math]::Round($_.Length/1GB, 3)}}
```

## Variável alvo e tipo de tarefa

| Campo | Valor |
|-------|--------|
| **Variável alvo** | `rain_label` |
| **Tipo** | **Classificação** (rótulo de chuva / precipitação discretizada conforme definido no dataset). |
| **Métrica principal planeada** | **F1-score (macro)** como métrica principal de referência; **AUROC** como métrica secundária se o problema for binário de forma estável nas classes. |

*Alternativa documentada e não escolhida para o trabalho principal:* regressão com alvo `precip_mm` (métricas típicas MAE / RMSE) — permanece como extensão possível se o docente exigir mudança de alvo; neste registo o foco é **classificação com `rain_label`**.

## Aprovação do professor

- **Estado:** Aprovado para avanço da Parte 2 (EDA e pré-processamento) sobre o **Indian Weather**.
- **Data de registo:** 2026-04-22.
- **Meio / forma:** confirmação do docente (canal acordado com a turma: presencial, Teams ou e-mail institucional). *Não publicar conteúdo sensível de e-mail no repositório; basta esta referência para a equipa e revisor.*

## Ligações

- Tarefa: [storyline/tasks/T020-dataset-aprovacao-alvo.md](../../storyline/tasks/T020-dataset-aprovacao-alvo.md)
- Marco: [storyline/milestones/M02-dados-aprovados-eda.md](../../storyline/milestones/M02-dados-aprovados-eda.md)
- História: [storyline/storys/S02-parte2-eda-preprocessamento.md](../../storyline/storys/S02-parte2-eda-preprocessamento.md)
