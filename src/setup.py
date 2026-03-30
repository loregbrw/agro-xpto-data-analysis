import subprocess
from rich.console import Console
from rich.panel import Panel

console = Console()

console.print(Panel.fit("[bold cyan]Agro XPTO Data Pipeline[/bold cyan]"))

console.log("[bold yellow]Downloading data...[/bold yellow]")
subprocess.run(["python", "src/download_data.py"], check=True)

console.log("[bold yellow]Running ingest...[/bold yellow]")
subprocess.run(["python", "src/ingest.py"], check=True)

console.log("[bold yellow]Running normalize...[/bold yellow]")
subprocess.run(["python", "src/normalize.py"], check=True)

console.log("[bold yellow]Getting USD/BRL values from Banco Central...[/bold yellow]")
subprocess.run(["python", "src/exchange_rate.py"], check=True)

console.log("[bold yellow]Linking USD/BRL values...[/bold yellow]")
subprocess.run(["python", "src/link_usd_with_brl.py"], check=True)

console.print(Panel.fit("[bold green]Pipeline finished successfully![/bold green]"))