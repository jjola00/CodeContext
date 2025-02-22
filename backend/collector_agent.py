import psutil
import requests
import os
import time
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
        try:
            metrics = collect_metrics()
            response = requests.post(f"{AGGREGATOR_API}/upload", json=metrics, timeout=5)
            if response.status_code == 200:
                print("Metrics Sent Successfully")
            else:
                print(f"Failed to send metrics: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending metrics: {e}")
        time.sleep(5)

if __name__ == "__main__":
    send_metrics()