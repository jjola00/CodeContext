from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import subprocess
import supabase
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"], 
)

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
db_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)
aggregator_process = None

@app.post("/upload")
def upload_metrics(metrics: dict):
    device_name = metrics.get("device_name")
    cpu_usage = metrics.get("cpu_usage")
    ram_usage = metrics.get("ram_usage")

    if not device_name or cpu_usage is None or ram_usage is None:
        raise HTTPException(status_code=400, detail="Missing required fields: device_name, cpu_usage, ram_usage")

    device_response = db_client.table("devices").select("id").eq("name", device_name).execute()
    if device_response.data:
        device_id = device_response.data[0]["id"]
    else:
        device_response = db_client.table("devices").insert({"name": device_name}).execute()
        device_id = device_response.data[0]["id"]

    metric_ids = db_client.table("metrics").select("id, name").in_("name", ["cpu_usage", "ram_usage"]).execute()
    metric_map = {m["name"]: m["id"] for m in metric_ids.data}

    if "cpu_usage" not in metric_map or "ram_usage" not in metric_map:
        raise HTTPException(status_code=500, detail="Metrics (cpu_usage, ram_usage) not found in database")

    db_client.table("device_metrics").insert([
        {"device_id": device_id, "metric_id": metric_map["cpu_usage"], "value": cpu_usage},
        {"device_id": device_id, "metric_id": metric_map["ram_usage"], "value": ram_usage},
    ]).execute()

    return {"message": "Metrics stored successfully"}

@app.get("/metrics")
def get_metrics():
    try:
        response = db_client.table("device_metrics") \
            .select("value, timestamp, devices(name), metrics(name, unit)") \
            .order("timestamp", desc=True) \
            .limit(20) \
            .execute()

        if not response.data:
            raise HTTPException(status_code=404, detail="No metrics found")

        return [
            {
                "device_name": row["devices"]["name"],
                "metric_name": row["metrics"]["name"],
                "value": row["value"],
                "unit": row["metrics"]["unit"],
                "timestamp": row["timestamp"]
            }
            for row in response.data
        ]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving metrics: {e}")
    
@app.post("/start-collector")
def start_collector():
    global aggregator_process
    aggregator_process = subprocess.Popen(["python", "collector_agent.py"])
    return {"message": "Collector agent started"}

@app.post("/stop-collector")
def stop_collector():
    global aggregator_process
    if aggregator_process:
        aggregator_process.terminate()
        aggregator_process = None
        return {"message": "Collector agent stopped"}
    else:
        raise HTTPException(status_code=400, detail="Collector agent is not running")