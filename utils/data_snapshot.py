import psutil
import threading
import time
from datetime import datetime
from pydantic import BaseModel

class DataSnapshot(BaseModel):
    timestamp: datetime
    cpu_usage: float
    ram_usage: float

    @staticmethod
    def capture():
        return DataSnapshot(
            timestamp=datetime.now(),
            cpu_usage=psutil.cpu_percent(interval=1),
            ram_usage=psutil.virtual_memory().percent
        )

# Cache Implementation
cache_lock = threading.Lock()
cached_data = None
last_read_time = None

def get_cached_metrics():
    global cached_data, last_read_time
    with cache_lock:
        if cached_data is None or (time.time() - last_read_time) >= 30:
            cached_data = DataSnapshot.capture()
            last_read_time = time.time()
    return cached_data, datetime.now()  # Return cached data + response timestamp
