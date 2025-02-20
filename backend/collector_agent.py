import psutil
import requests
import os
from time import sleep

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
AGGREGATOR_API = os.getenv("AGGREGATOR_API")


def collect_metrics():
    metrics = {
        "cpu_usage": psutil.cpu_percent(interval=1),
        "ram_usage": psutil.virtual_memory().percent,
    }
    return metrics

def send_metrics():
    while True:
        metrics = collect_metrics()
        response = requests.post(f"{AGGREGATOR_API}/upload", json=metrics)
        print("Metrics Sent:", response.status_code)
        sleep(5)

if __name__ == "__main__":
    send_metrics()