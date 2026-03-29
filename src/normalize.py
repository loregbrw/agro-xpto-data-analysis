import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

fact_exports = pd.read_csv(PROCESSED / "unified_data.csv")

#Type conversion

print("Converting types")

fact_exports["CO_ANO"] = pd.to_numeric(fact_exports["CO_ANO"], errors="coerce")
fact_exports["CO_MES"] = pd.to_numeric(fact_exports["CO_MES"], errors="coerce")
fact_exports["CO_NCM"] = pd.to_numeric(fact_exports["CO_NCM"], errors="coerce")
fact_exports["CO_PAIS"] = pd.to_numeric(fact_exports["CO_PAIS"], errors="coerce")
fact_exports["VL_FOB"] = pd.to_numeric(fact_exports["VL_FOB"], errors="coerce")
fact_exports["KG_LIQUIDO"] = pd.to_numeric(fact_exports["KG_LIQUIDO"], errors="coerce")
fact_exports["QT_ESTAT"] = pd.to_numeric(fact_exports["QT_ESTAT"], errors="coerce")

#Clean fact Table

print("Cleaning fact table")


fact_exports = fact_exports.drop_duplicates()

fact_exports = fact_exports.dropna(subset=[
    "CO_ANO",
    "CO_MES",
    "CO_NCM",
    "CO_PAIS",
    "VL_FOB"
])

fact_exports = fact_exports[
    (fact_exports["CO_MES"] >= 1) &
    (fact_exports["CO_MES"] <= 12)
]

fact_exports = fact_exports[fact_exports["VL_FOB"] >= 0]

fact_exports["CO_ANO"] = fact_exports["CO_ANO"].astype("int16")
fact_exports["CO_MES"] = fact_exports["CO_MES"].astype("int8")

#Clean dimensions

print("Cleaning dimensions")

dim_ncm = pd.read_csv(RAW / "NCM.csv", sep=";", encoding="latin1")
dim_pais = pd.read_csv(RAW / "PAIS.csv", sep=";", encoding="latin1")
dim_uf = pd.read_csv(RAW / "UF.csv", sep=";", encoding="latin1")
dim_via = pd.read_csv(RAW / "VIA.csv", sep=";", encoding="latin1")

dim_urf = pd.read_csv(
    RAW / "URF.csv",
    sep=";",
    encoding="latin1",
    dtype={"CO_URF": str}
)

dim_ncm = dim_ncm.drop_duplicates()
dim_pais = dim_pais.drop_duplicates()
dim_uf = dim_uf.drop_duplicates()
dim_via = dim_via.drop_duplicates()
dim_urf = dim_urf.drop_duplicates()

invalid_pais = (~fact_exports["CO_PAIS"].isin(dim_pais["CO_PAIS"])).sum()
invalid_ncm = (~fact_exports["CO_NCM"].isin(dim_ncm["CO_NCM"])).sum()

fact_exports.to_csv(PROCESSED / "fact_exportacoes.csv", index=False)

dim_ncm.to_csv(PROCESSED / "dim_ncm.csv", index=False)
dim_pais.to_csv(PROCESSED / "dim_pais.csv", index=False)
dim_uf.to_csv(PROCESSED / "dim_uf.csv", index=False)
dim_via.to_csv(PROCESSED / "dim_via.csv", index=False)
dim_urf.to_csv(PROCESSED / "dim_urf.csv", index=False)

print("Normalization complete!")
print("Final fact shape:", fact_exports.shape)

