import threading
import time
import logging

logger = logging.getLogger(__name__)

class CacheUpdateManager:
    """RAII-style cache lock manager to ensure safe updates."""
    def __init__(self, lock):
        self.lock = lock
        self.active_update_start_time = None

    def __enter__(self):
        self.lock.acquire()
        self.active_update_start_time = time.time()
        logger.debug(f"Cache update started at {self.active_update_start_time}")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        logger.debug(f"Cache update completed in {time.time() - self.active_update_start_time:.3f} seconds")
        self.lock.release()

# Global Lock
cache_lock = threading.Lock()

def spin_wait_for_lock():
    """Spin wait for lock acquisition with CPU vs Responsiveness balance"""
    while not cache_lock.acquire(blocking=False):
        logger.debug("Waiting for cache lock...")
        time.sleep(0.1)  # Avoid CPU overuse
    return CacheUpdateManager(cache_lock)
