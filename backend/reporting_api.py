from fastapi import FastAPI
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
    response = db_client.table("metrics").select("*").execute()
    return response.data