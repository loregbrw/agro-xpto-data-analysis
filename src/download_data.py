import requests
from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn

console = Console()

RAW = Path("data/raw")
PROCESSED = Path("data/processed")

RAW.mkdir(parents=True, exist_ok=True)
PROCESSED.mkdir(parents=True, exist_ok=True)

console.print(Panel.fit("[bold cyan]Downloading Agro XPTO datasets[/bold cyan]"))

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

with Progress(
    SpinnerColumn(),
    TextColumn("[bold yellow]{task.description}"),
    BarColumn(),
    console=console
) as progress:

    for filename, url in files.items():

        path = RAW / filename

        if path.exists():
            console.log(f"[blue]{filename} already exists, skipping[/blue]")
            continue

        task = progress.add_task(f"Downloading {filename}", total=None)

        try:
            with requests.get(url, stream=True, verify=False) as r:
                r.raise_for_status()

                with open(path, "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)

            progress.update(task, completed=1)
            console.log(f"[green]{filename} downloaded successfully[/green]")

        except Exception as e:
            console.log(f"[red]Error downloading {filename}: {e}[/red]")

console.print(Panel.fit("[bold green]Download complete![/bold green]"))