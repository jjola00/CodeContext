import psutil
import threading
import time
from datetime import datetime
from pydantic import BaseModel
from utils.cache_manager import CacheUpdateManager, spin_wait_for_lock

class DataSnapshot(BaseModel):
    timestamp: datetime
    cpu_usage: float
    ram_usage: float

    @staticmethod
    def capture():
        """Simulate slow data reading (5s delay) and return system metrics."""
        time.sleep(5)  # Simulate slow data reading (>5s)
        return DataSnapshot(
            timestamp=datetime.now(),
            cpu_usage=psutil.cpu_percent(interval=1),
            ram_usage=psutil.virtual_memory().percent
        )

# Cache Implementation
cached_data = None
last_read_time = None

def get_cached_metrics():
    """Retrieve cached metrics if recent, otherwise refresh data."""
    global cached_data, last_read_time
    with spin_wait_for_lock():  # Ensures proper locking with spin wait
        if cached_data is None or (time.time() - last_read_time) >= 30:
            cached_data = DataSnapshot.capture()
            last_read_time = time.time()
            assert cached_data is not None, "Cache update failed!"
    return cached_data, datetime.now()  # Return cached data + response timestamp
