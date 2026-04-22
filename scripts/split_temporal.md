# `split_temporal.py` — Split temporal reprodutível (T021)

## Objetivo

Definir cortes **treino / validação / teste** de forma **reprodutível**, ordenando o dataset pela coluna **`datetime`** (ordem ascendente, `mergesort` estável) e aplicando **frações fixas** ao número de linhas após ordenação. O script lê **apenas** `datetime` do Parquet para reduzir memória.

## Onde corre

No **host**, com venv e `pip install -r requirements.txt` (precisa de **pandas** + **pyarrow**).

## Uso

Na raiz do repositório:

```powershell
python scripts\split_temporal.py
```

Com Parquet explícito:

```powershell
python scripts\split_temporal.py -i data\Indian_Weather_Dataset.parquet
```

Frações personalizadas (devem somar 1.0):

```powershell
python scripts\split_temporal.py --train 0.8 --val 0.1 --test 0.1 --seed 42
```

## Argumentos

| Argumento | Descrição |
|-----------|------------|
| `-i`, `--input` | Caminho do Parquet (por defeito: `data/Indian_Weather_Dataset.parquet` na raiz do repo). |
| `--train`, `--val`, `--test` | Frações em ponto flutuante (por defeito 0,70 / 0,15 / 0,15). |
| `--seed` | Seed de `random` (por defeito 42); o split **não** usa shuffle — serve para reprodutibilidade do ambiente. |

## Saída

- Tabela Markdown: split, número de linhas, `min(datetime)`, `max(datetime)`.
- Checagens textuais nas fronteiras treino→validação→teste.
- Lista de **riscos de data leakage** a evitar nas fases seguintes (pré-processamento, modelagem).
- Versão do **pandas** (registar na evidência da T021).

## Colunas usadas

- **Ordenação e cortes:** apenas `datetime`.
- O alvo (`rain_label`, T020) **não** entra no split neste script; todas as linhas são partidas pelo tempo da mesma forma.

## Timestamps duplicados

Se muitas linhas partilharem o mesmo `datetime`, a fronteira pode cortar **no meio** de um instante: parte das linhas com o mesmo timestamp pode cair em splits diferentes. O script avisa na secção de leakage; para estratégias alternativas (ex.: agrupar por `(datetime, state, city)`), documentar noutro artefacto (T022).

## Ver também

- [T021 no storyline](../storyline/tasks/T021-split-temporal-leakage.md)
- [Aprovação / alvo T020](../organization/evidencias/aprovacao.md)
- [README dos scripts](README.md)
