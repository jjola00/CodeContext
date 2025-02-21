from fastapi import FastAPI, HTTPException
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
DEVICE_API = os.getenv("DEVICE_API")

@app.post("/restart")
def restart_device():
    if not DEVICE_API:
        raise HTTPException(status_code=500, detail="DEVICE_API is not set")

    try:
        response = requests.post(f"{DEVICE_API}/restart", timeout=5)
        response.raise_for_status()
        return {"message": "Device restart command sent", "status": response.status_code}
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Failed to restart device: {e}")
