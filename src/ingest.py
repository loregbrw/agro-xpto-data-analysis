import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

files = [
    "EXP_2021.csv",
    "EXP_2022.csv",
    "EXP_2023.csv",
    "EXP_2024.csv",
    "EXP_2025.csv"
]

dfs = []

for file in files:
    print(f"Loading {file}")
    df = pd.read_csv(RAW / file, sep=";")
    dfs.append(df)

exported = pd.concat(dfs, ignore_index=True)
print(f"Exported lines: {exported.shape}")
print(exported.head)
exported.to_csv(PROCESSED / "unified_data.csv", index=False)