import subprocess
import time

scripts = ["collector_agent.py", "aggregator_api.py", "reporting_api.py"]

processes = []
for script in scripts:
    print(f"Starting {script}...")
    proc = subprocess.Popen(["python", script])
    processes.append(proc)
    time.sleep(2) 

try:
    for proc in processes:
        proc.wait()
except KeyboardInterrupt:
    print("Shutting down all processes...")
    for proc in processes:
        proc.terminate()
