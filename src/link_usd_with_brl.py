import pandas as pd
from pathlib import Path
from rich.console import Console
from rich.panel import Panel

console = Console()

PROCESSED = Path("data/processed")
RAW = Path("data/raw")

console.print(Panel.fit("[bold cyan]Linking USD/BRL exchange rates to export data[/bold cyan]"))

console.log("[yellow]Loading datasets...[/yellow]")

fact = pd.read_csv(PROCESSED / "fact_exported.csv")
fx = pd.read_csv(RAW / "usd_brl_daily.csv")

console.log(f"[blue]Fact rows:[/blue] {len(fact)}")
console.log(f"[blue]FX rows:[/blue] {len(fx)}")

console.log("[yellow]Preparing exchange rate data...[/yellow]")

fx["date"] = pd.to_datetime(fx["date"])

fx["CO_ANO"] = fx["date"].dt.year
fx["CO_MES"] = fx["date"].dt.month

fx_monthly = (
    fx.groupby(["CO_ANO", "CO_MES"])["usd_brl"]
    .mean()
    .reset_index()
)

console.log("[yellow]Merging exchange rates with export data...[/yellow]")

fact = fact.merge(
    fx_monthly,
    on=["CO_ANO", "CO_MES"],
    how="left"
)

# Resolver conflito de colunas caso exista
if "usd_brl_x" in fact.columns:
    fact["usd_brl"] = fact["usd_brl_y"]
    fact = fact.drop(columns=["usd_brl_x", "usd_brl_y"])

console.log("[yellow]Calculating export values in BRL...[/yellow]")

fact["VL_FOB_BRL"] = fact["VL_FOB"] * fact["usd_brl"]

missing_fx = fact["usd_brl"].isna().sum()

if missing_fx > 0:
    console.log(f"[red]Warning:[/red] {missing_fx} rows without exchange rate")

console.log("[yellow]Saving updated fact table...[/yellow]")

fact.to_csv(PROCESSED / "fact_exported.csv", index=False)

console.print(Panel.fit("[bold green]BRL values successfully added to fact table![/bold green]"))

console.log(f"[bold blue]Final rows:[/bold blue] {len(fact)}")