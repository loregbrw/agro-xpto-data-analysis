import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw")

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
    df = pd.read_csv(DATA_PATH / file, sep=";")
    dfs.append(df)

exported = pd.concat(dfs, ignore_index=True)
print(exported.shape)