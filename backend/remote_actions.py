# remote_actions.py
from fastapi import FastAPI
import os
import requests

app = FastAPI()
DEVICE_API = os.getenv("DEVICE_API")

@app.post("/restart")
def restart_device():
    response = requests.post(f"{DEVICE_API}/restart")
    return {"message": "Device restart command sent", "status": response.status_code}