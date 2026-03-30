import requests
import pandas as pd
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

RAW = Path("data/raw")
RAW.mkdir(parents=True, exist_ok=True)

console.print(Panel.fit("[bold cyan]Downloading USD/BRL Exchange Rates[/bold cyan]"))

url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.1/dados"

params = {
    "formato": "json",
    "dataInicial": "01/01/2021",
    "dataFinal": "31/12/2025"
}

console.log("[yellow]Requesting exchange rate data from Banco Central...[/yellow]")

response = requests.get(url, params=params)
response.raise_for_status()

data = response.json()

console.log("[yellow]Processing dataset...[/yellow]")

df = pd.DataFrame(data)

df["data"] = pd.to_datetime(df["data"], dayfirst=True)
df["valor"] = df["valor"].astype(float)

df = df.rename(columns={
    "data": "date",
    "valor": "usd_brl"
})

df = df.sort_values("date")

output = RAW / "usd_brl_daily.csv"

console.log("[yellow]Saving dataset...[/yellow]")

df.to_csv(output, index=False)

console.print(Panel.fit("[bold green]Exchange rate dataset created successfully![/bold green]"))

console.log(f"[bold blue]Saved to:[/bold blue] {output}")
console.log(f"[bold blue]Rows:[/bold blue] {len(df)}")