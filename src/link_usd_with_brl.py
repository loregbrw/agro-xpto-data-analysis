import pandas as pd
from pathlib import Path

PROCESSED = Path("data/processed")
RAW = Path("data/raw")

fact = pd.read_csv(PROCESSED / "fact_exported.csv")
fx = pd.read_csv(RAW / "usd_brl_daily.csv")

fx["date"] = pd.to_datetime(fx["date"])

fx["CO_ANO"] = fx["date"].dt.year
fx["CO_MES"] = fx["date"].dt.month

fx_monthly = (
    fx.groupby(["CO_ANO","CO_MES"])["usd_brl"]
    .mean()
    .reset_index()
)

fact = fact.merge(
    fx_monthly,
    on=["CO_ANO","CO_MES"],
    how="left"
)

# resolver possível duplicação
if "usd_brl_x" in fact.columns:
    fact["usd_brl"] = fact["usd_brl_y"]
    fact = fact.drop(columns=["usd_brl_x","usd_brl_y"])

fact["VL_FOB_BRL"] = fact["VL_FOB"] * fact["usd_brl"]

fact.to_csv(PROCESSED / "fact_exported.csv", index=False)

print("BRL values added to fact table!")