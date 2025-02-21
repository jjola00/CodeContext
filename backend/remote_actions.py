# remote_actions.py
from fastapi import FastAPI
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
DEVICE_API = os.getenv("DEVICE_API")

@app.post("/restart")
def restart_device():
    if not DEVICE_API:
        return {"error": "DEVICE_API is not set"}
    
    response = requests.post(f"{DEVICE_API}/restart")  
    return {"message": "Device restart command sent", "status": response.status_code}