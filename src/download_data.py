import requests
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")
RAW.mkdir(parents=True, exist_ok=True)
PROCESSED.mkdir(parents=True, exist_ok=True)

files = {
    # exportações
    "EXP_2021.csv": "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2021.csv",
    "EXP_2022.csv": "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2022.csv",
    "EXP_2023.csv": "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2023.csv",
    "EXP_2024.csv": "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2024.csv",
    "EXP_2025.csv": "https://balanca.economia.gov.br/balanca/bd/comexstat-bd/ncm/EXP_2025.csv",

    # tabelas auxiliares
    "NCM.csv": "https://balanca.economia.gov.br/balanca/bd/tabelas/NCM.csv",
    "PAIS.csv": "https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS.csv",
    "PAIS_BLOCO.csv": "https://balanca.economia.gov.br/balanca/bd/tabelas/PAIS_BLOCO.csv",
    "UF.csv": "https://balanca.economia.gov.br/balanca/bd/tabelas/UF.csv",
    "UF_MUN.csv": "https://balanca.economia.gov.br/balanca/bd/tabelas/UF_MUN.csv",
    "VIA.csv": "https://balanca.economia.gov.br/balanca/bd/tabelas/VIA.csv",
    "URF.csv": "https://balanca.economia.gov.br/balanca/bd/tabelas/URF.csv",
}

for filename, url in files.items():

    path = RAW / filename

    if path.exists():
        print(f"{filename} already exists, skipping...")
        continue

    print(f"Downloading {filename}...")

    try:
        with requests.get(url, stream=True, verify=False) as r:
            r.raise_for_status()

            with open(path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

        print(f"{filename} downloaded successfully!")

    except Exception as e:
        print(f"Error downloading {filename}: {e}")

print("Download complete!")