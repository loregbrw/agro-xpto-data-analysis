import requests
import pandas as pd
from pathlib import Path 

RAW = Path("data/raw")
RAW.mkdir(parents=True, exist_ok=True)

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados"

params = {
    "formato": "json",
    "dataInicial": "01/01/2021",
    "dataFinal": "31/12/2025"
}

print("Dowload USD/BRL data from Banco Central...")

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

df = pd.DataFrame(data)

df["data"] = pd.to_datetime(df["data"], dayfirst=True)
df["valor"] = df["valor"].astype(float)

df = df.rename(columns={
    "data": "date",
    "valor": "usd_brl"
})

df = df.sort_values("date")
output = RAW / "usd_brl_daily.csv"

df.to_csv(output, index=False)

print("Exchange rate dataset created!")
print(f"Saved to: {output}")
print(f"Rows: {len(df)}")
