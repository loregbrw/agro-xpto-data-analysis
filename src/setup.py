import subprocess

print("Downloading data...")
subprocess.run(["python", "src/download_data.py"], check=True)

print("Running ingest...")
subprocess.run(["python", "src/ingest.py"], check=True)

print("Running normalize...")
subprocess.run(["python", "src/normalize.py"], check=True)

print("Pipeline finished!")