# Changelog: streaming de CSV para Parquet (PyArrow)

**Data:** 2026-04-21  
**Área:** ferramentas / pipeline de dados  
**Arquivo principal:** [scripts/csv_to_parquet.py](../../scripts/csv_to_parquet.py)

## Resumo

Foi adicionado um script de **linha de comando** que converte CSVs **muito grandes** (incluindo o dataset Indian Weather) para **Parquet** com leitura **em streaming** via **PyArrow** e escrita **em lotes**, sem carregar o CSV inteiro na RAM.

## Motivação

O CSV do Indian Weather tem **vários gigabytes**. Uma abordagem ingênua com `read_csv` pode causar **OOM** (falta de memória) em laptops comuns. O processamento em **lotes** mantém o pico de memória controlado e ainda assim gera **um único** arquivo Parquet de saída.

## O que mudou

| Item | Detalhe |
|------|---------|
| Script | `scripts/csv_to_parquet.py` — `convert_csv_to_parquet()` usa `pyarrow.csv.open_csv`, `read_next_batch()` e `pyarrow.parquet.ParquetWriter.write_table()` por lote |
| Dependências | [requirements.txt](../../requirements.txt) — `pyarrow>=14.0.0` |
| Fim de arquivo | O PyArrow sinaliza fim de stream com **`StopIteration`** em `read_next_batch()`; o laço captura essa exceção (só checar lote vazio nem sempre basta) |
| Padrões | Entrada: `data/archive/Indian_Weather_Dataset.csv`; saída: `data/archive/Indian_Weather_Dataset.parquet` (caminhos resolvidos a partir da raiz do repositório pela lógica de `Path` em `main`) |

Observação: o repositório pode manter Parquet em `data/Indian_Weather_Dataset.parquet`; ajuste `-i`/`-o` se a sua estrutura de pastas for outra.

## Como executar

```powershell
Set-Location c:\Desenvolvimento\BigData
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\csv_to_parquet.py --help
```

Consulte a seção **How to run (CSV to Parquet)** no [README.md](../../README.md) para as flags (`-i`, `-o`, `--compression`, `--read-block-mib`).

## Verificação

- Executar `python scripts\csv_to_parquet.py --help` após `pip install -r requirements.txt`.
- Teste de fumaça com um CSV pequeno: confirmar que a contagem de linhas da saída bate com a entrada.

## Riscos / limitações

- Várias chamadas a `write_table` ainda produzem **um único arquivo** Parquet, mas o **layout de row groups** depende do tamanho dos lotes; costuma ser adequado para análises; reajuste `read_block_mib` se necessário.
- A conversão **do dataset completo** pode levar muito tempo e exigir bastante **I/O** em disco.

## Próximos passos (opcional)

- Adicionar opção de **tamanho de row group** / **máximo de linhas por arquivo** para tabelas muito largas.
- Documentar **overrides de dtype** esperados se o PyArrow inferir tipos de forma diferente do esperado por fluxos baseados em pandas.
