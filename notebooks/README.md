# Notebooks (EDA)

## Pré-requisitos

1. Ambiente virtual na raiz do repositório (ver [README.md](../README.md)).
2. `pip install -r requirements.txt`
3. Ficheiro local `data/Indian_Weather_Dataset.parquet` (não versionado no Git).

## Como executar

```powershell
cd c:\Desenvolvimento\BigData
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
jupyter lab
```

Abrir `notebooks/eda.ipynb`, executar **Run All**. As figuras PNG são gravadas em `notebooks/figuras/` (pasta versionada com `.gitkeep`; as imagens geradas ficam no disco local).
