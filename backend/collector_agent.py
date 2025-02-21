import psutil
import requests
import os
from time import sleep
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
AGGREGATOR_API = os.getenv("AGGREGATOR_API")
DEVICE_NAME = os.getenv("DEVICE_NAME") 

if not AGGREGATOR_API or not DEVICE_NAME:
    raise ValueError("AGGREGATOR_API or DEVICE_NAME is not set")

def collect_metrics():
    metrics = {
        "device_name": DEVICE_NAME,
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