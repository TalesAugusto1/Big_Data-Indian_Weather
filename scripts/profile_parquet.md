# `profile_parquet.py` — Perfil agregado do Parquet (PyArrow)

## Objetivo

Gerar uma **tabela Markdown** com, por coluna: **tipo**, **número de linhas**, **nulos**, **% nulos**, **valores distintos** (com amostra opcional), **min** / **max** quando aplicável.  
Útil para **fundamentar** decisões de missing, cardinalidade e scaling em [`docs/preprocessamento.md`](../docs/preprocessamento.md) (T022) e na EDA (T024), **sem pandas** nem **scikit-learn**.

## Onde corre

No **host**, com `pip install -r requirements.txt` (só **pyarrow**).

## Uso

```powershell
python scripts\profile_parquet.py -i data\Indian_Weather_Dataset.parquet
```

Só algumas colunas:

```powershell
python scripts\profile_parquet.py -i data\Indian_Weather_Dataset.parquet --columns datetime,rain_label,city,state
```

Contagem de **distintos** no ficheiro inteiro (pode ser **muito lento** em colunas enormes):

```powershell
python scripts\profile_parquet.py -i data\Indian_Weather_Dataset.parquet --distinct-sample-rows 0
```

## Parâmetros

| Argumento | Descrição |
|-----------|------------|
| `-i`, `--input` | Caminho do Parquet. |
| `--columns` | Lista separada por vírgulas; vazio = todas. |
| `--distinct-sample-rows` | Máximo de linhas por coluna usadas na contagem de distintos (por defeito `1000000`). `0` = tentar coluna completa. |

## Limitações

- Cada coluna é lida **em separado** do disco (várias leituras).
- `distintos` em strings de **alta cardinalidade** com amostra é **aproximado** (serve para ordem de grandeza).
- Colunas com erro de leitura aparecem com `ERRO` na linha.

## Ver também

- [split_temporal.md](split_temporal.md) (T021)
- [preprocessamento.md](../docs/preprocessamento.md) (T022)
