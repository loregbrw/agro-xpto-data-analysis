import pandas as pd
from pathlib import Path
from rich.console import Console
from rich.progress import track
from rich.panel import Panel

console = Console()

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

files = [
    "EXP_2021.csv",
    "EXP_2022.csv",
    "EXP_2023.csv",
    "EXP_2024.csv",
    "EXP_2025.csv"
]

console.print(Panel.fit("[bold cyan]Starting Data Ingestion[/bold cyan]"))

dfs = []

for file in track(files, description="[yellow]Loading export files..."):
    path = RAW / file
    console.log(f"Reading [bold]{file}[/bold]")
    
    df = pd.read_csv(path, sep=";")
    dfs.append(df)

console.log("[green]All files loaded successfully[/green]")

console.log("[yellow]Concatenating datasets...[/yellow]")
exported = pd.concat(dfs, ignore_index=True)

console.log(f"[bold blue]Total rows:[/bold blue] {exported.shape[0]}")

console.log("[yellow]Saving unified dataset...[/yellow]")
exported.to_csv(PROCESSED / "unified_data.csv", index=False)

console.print(Panel.fit("[bold green]Unified dataset created successfully![/bold green]"))