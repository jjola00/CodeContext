from fastapi import FastAPI, HTTPException
import supabase
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
db_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

@app.post("/upload")
def upload_metrics(metrics: dict):
    device_name = metrics.get("device_name")
    cpu_usage = metrics.get("cpu_usage")
    ram_usage = metrics.get("ram_usage")

    if not device_name or cpu_usage is None or ram_usage is None:
        raise HTTPException(status_code=400, detail="Missing required fields: device_name, cpu_usage, ram_usage")

    device_response = db_client.table("devices").select("*").eq("name", device_name).execute()
    if not device_response.data:
        device_response = db_client.table("devices").insert({"name": device_name}).execute()
        device_id = device_response.data[0]["id"]
    else:
        device_id = device_response.data[0]["id"]

    cpu_metric_response = db_client.table("metrics").select("*").eq("name", "cpu_usage").execute()
    ram_metric_response = db_client.table("metrics").select("*").eq("name", "ram_usage").execute()

    if not cpu_metric_response.data or not ram_metric_response.data:
        raise HTTPException(status_code=500, detail="Metrics (cpu_usage, ram_usage) not found in database")

    cpu_metric_id = cpu_metric_response.data[0]["id"]
    ram_metric_id = ram_metric_response.data[0]["id"]

    db_client.table("device_metrics").insert([
        {"device_id": device_id, "metric_id": cpu_metric_id, "value": cpu_usage},
        {"device_id": device_id, "metric_id": ram_metric_id, "value": ram_usage},
    ]).execute()

    return {"message": "Metrics stored successfully"}