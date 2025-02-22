from fastapi import FastAPI, HTTPException
import supabase
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
db_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/metrics")
def get_metrics():
    response = db_client.table("device_metrics") \
        .select("value, timestamp, devices(name), metrics(name, unit)") \
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