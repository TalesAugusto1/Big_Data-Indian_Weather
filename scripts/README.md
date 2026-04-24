# Scripts do repositório

Ferramentas de linha de comandos para preparar dados e validar o stack Docker (M01).

| Script | Onde corre | Documentação |
|--------|------------|----------------|
| [`csv_to_parquet.py`](csv_to_parquet.py) | **Host** (Python + venv) | [csv_to_parquet.md](csv_to_parquet.md) |
| [`split_temporal.py`](split_temporal.py) | **Host** (Python + venv; M02 / T021) | [split_temporal.md](split_temporal.md) |
| [`t012_smoke_parquet.py`](t012_smoke_parquet.py) | **Dentro do contentor Spark** (via `spark-submit`) | [t012_smoke_parquet.md](t012_smoke_parquet.md) |

## Pré-requisito comum (host)

Para `csv_to_parquet.py`:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Instruções completas de venv: [README.md](../README.md#ambiente-virtual-python) na raiz do repositório.

## Ligações úteis

- Pipeline de pré-processamento (M02 / T022): [../docs/preprocessamento.md](../docs/preprocessamento.md)
- Stack Docker e smoke T012: [../docker/README.md](../docker/README.md)
- Guia operacional aprofundado: [../docs/guides/stack-completo-e-dados.md](../docs/guides/stack-completo-e-dados.md)
- Changelog CSV→Parquet: [../docs/changelog/2026-04-21-csv-to-parquet-streaming.md](../docs/changelog/2026-04-21-csv-to-parquet-streaming.md)
- Changelog smoke T012: [../docs/changelog/2026-04-21-t012-dataset-smoke.md](../docs/changelog/2026-04-21-t012-dataset-smoke.md)
