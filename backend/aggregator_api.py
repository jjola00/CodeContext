from fastapi import FastAPI
import supabase
import os

app = FastAPI()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
db_client = supabase.create_client(SUPABASE_URL, SUPABASE_KEY)

@app.post("/upload")
def upload_metrics(metrics: dict):
    db_client.table("metrics").insert(metrics).execute()
    return {"message": "Metrics stored successfully"}