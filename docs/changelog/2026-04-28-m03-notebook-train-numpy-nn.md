# Changelog: M03 — Notebook `neural_network_numpy_training` (rede NumPy + PyArrow)

**Data:** 2026-04-28  
**Área:** Storyline M03 / S03 / Parte 3 (rede neural)  
**Storyline:** [T033](../../storyline/tasks/T033-rede-neural.md) (artefacto de referência)  
**Branch:** `trainnumpy`

## Resumo

Notebook **[`notebooks/neural_network_numpy_training.ipynb`](../../notebooks/neural_network_numpy_training.ipynb)** com MLP em **NumPy** (BCE + sigmoid na saída), leitura em batches com **PyArrow Dataset**, **one-hot** para `state` / `city` / `crops`, normalização com estatísticas **só no treino**, e avaliação no val/teste. O trabalho corrige falhas que geravam **loss `nan`**, avisos de **média em slice vazio** e desalinhamento com o **split temporal T021**.

## Motivação

- Entregável reprodutível para **T033** sem dependência de Keras/PyTorch no host.
- Garantir o **mesmo critério temporal** que [`scripts/split_temporal.py`](../../scripts/split_temporal.py) (70/15/15 sobre `datetime` ordenado).
- Tornar o notebook **robusto ao cwd** do Jupyter (`./data/` vs `../data/`).

## O que mudou

| Item | Detalhe |
|------|---------|
| [`notebooks/neural_network_numpy_training.ipynb`](../../notebooks/neural_network_numpy_training.ipynb) | `resolve_data_parquet()`; `temporal_split_filters()` alinhado ao T021; `get_stats()` com `nanmean`/`nanstd` e erro se treino vazio; `to_xy` com `dtype` inteiro nos índices one-hot, `nan_to_num` nas features; `bce` com `nanmean`; **MLP** com atualização de **biases** no `backward`; inicialização `default_rng(42)`; treino com erro explícito se não houver batches ou loss não finita. |

## Como verificar

1. Colocar `Indian_Weather_Dataset.parquet` em `data/` na raiz do repo.
2. Abrir o notebook; kernel Python com `pyarrow`, `numpy`, `matplotlib`.
3. Executar células por ordem. Esperado: linha `Split T021: ... | train rows: ...` com contagem **> 0** e épocas com **loss finita** (ordem ~0,69 no início, variando com dados).

```powershell
cd C:\Desenvolvimento\BigData
.\.venv\Scripts\Activate.ps1
# opcional: smoke do split oficial
python scripts\split_temporal.py -i data\Indian_Weather_Dataset.parquet
```

## Riscos e limites

- **`build_maps()`** percorre categorias no dataset completo (pode ser **lento** em máquinas modestas).
- O split por **fronteiras de `datetime`** pode cortar no meio de **timestamps duplicados** (mesmo aviso que no script T021).
- Rede manual: sem early stopping nem mixed precision; adequado a laboratório / laptop com batch pequeno.

## Follow-ups

- Registar **tempo de treino** e hardware na tarefa **T033** quando fechar critérios.
- Alinhar alvo e métricas ao protocolo **T030** se o projeto migrar totalmente para regressão (`temperature_C`).
