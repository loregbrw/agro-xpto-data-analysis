import subprocess

print("Downloading data...")
subprocess.run(["python", "src/download_data.py"], check=True)

print("Running ingest...")
subprocess.run(["python", "src/ingest.py"], check=True)

print("Running normalize...")
subprocess.run(["python", "src/normalize.py"], check=True)

print("Geting USD / BRL values from Banco Central...")
subprocess.run(["python", "src/exchange_rate.py"], check=True)

print("Linking USD / BRL values...")
subprocess.run(["python", "src/link_usd_with_brl.py"], check=True)

print("Pipeline finished!")