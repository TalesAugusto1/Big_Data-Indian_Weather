# `csv_to_parquet.py` — CSV para Parquet em streaming

## Objetivo

Converter um ficheiro **CSV** muito grande para **Parquet** usando **PyArrow**, lendo o CSV em **blocos** para não carregar o ficheiro inteiro na RAM. Adequado ao *Indian Weather* e a outros CSVs gigantes.

## Onde corre

No **host** (máquina de desenvolvimento), **não** dentro do Docker Spark. Requer dependências do [`requirements.txt`](../requirements.txt) (principalmente `pyarrow`).

## Caminhos por defeito

Relativamente à **raiz do repositório** (pai da pasta `scripts/`):

| | Caminho |
|---|---------|
| Entrada CSV | `data/archive/Indian_Weather_Dataset.csv` |
| Saída Parquet | `data/archive/Indian_Weather_Dataset.parquet` |

A pasta `data/` está no `.gitignore`; tem de existir localmente com o CSV (ou outro ficheiro que queira converter).

## Uso

Na raiz do repo, com o venv ativo:

```powershell
python scripts\csv_to_parquet.py
```

Com caminhos explícitos:

```powershell
python scripts\csv_to_parquet.py -i data\archive\Indian_Weather_Dataset.csv -o data\Indian_Weather_Dataset.parquet
```

macOS / Linux:

```bash
python scripts/csv_to_parquet.py -i data/archive/Indian_Weather_Dataset.csv -o data/Indian_Weather_Dataset.parquet
```

## Argumentos da linha de comandos

| Argumento | Descrição |
|-------------|-----------|
| `-i`, `--input` | Caminho do CSV de entrada (ficheiro). |
| `-o`, `--output` | Caminho do ficheiro Parquet de saída (cria diretórios pais se necessário). |
| `--compression` | Codec Parquet: `snappy`, `zstd` (**por defeito**), `gzip`, `lz4`, `brotli`. |
| `--read-block-mib N` | Tamanho do bloco do parser CSV em **mebibytes** (por defeito: `8`). Valores maiores podem acelerar leitura em disco rápido; valores menores reduzem pico de RAM. |

## Comportamento e saída

- Abre o CSV com `pyarrow.csv.open_csv` e lê **lotes** (`read_next_batch`) até ao fim.
- Abre o `ParquetWriter` na primeira tabela com esquema conhecido e acrescenta blocos.
- No **stderr** imprime algo como: `Wrote N rows to <destino>` (número de linhas com separador de milhares).
- Códigos de saída: `0` sucesso, `1` erro (ficheiro em falta ou exceção).

## Erros frequentes

| Situação | Causa provável |
|----------|----------------|
| `Input not found` | O caminho `-i` não existe ou não é ficheiro. |
| `Error: ...` | Permissões, disco cheio, CSV mal formado para o parser, etc. Ver mensagem completa no stderr. |

## Relação com o Docker / T012

O Parquet gerado no host deve ficar numa pasta montada no Spark, tipicamente **`data/`** na raiz do repo (montada como **`/dataset`** no contentor). O smoke [`t012_smoke_parquet.py`](t012_smoke_parquet.md) lê esse caminho dentro do contentor.

## Ver também

- [README.md na raiz](../README.md) — secção ambiente virtual e exemplos.
- [Changelog streaming CSV→Parquet](../docs/changelog/2026-04-21-csv-to-parquet-streaming.md)
