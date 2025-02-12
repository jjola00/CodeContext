import time
import logging
import ctypes 

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

class BlockTimer:
    """RAII-style performance timer using time.perf_counter()"""
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = (time.perf_counter() - self.start_time) * 1000  # Convert to milliseconds
        logger.info(f"Elapsed Time: {elapsed_time:.6f} milliseconds")

def simple_loop():
    for _ in range(100_000):
        pass

def function_call():
    def dummy_function():
        return 42
    for _ in range(100_000):
        dummy_function()

def os_api_call():
    kernel32 = ctypes.WinDLL("kernel32")  
    for _ in range(100_000):
        kernel32.GetTickCount() 
if __name__ == "__main__":
    logger.info("Starting Performance Timing...")

    with BlockTimer():
        simple_loop()

    with BlockTimer():
        function_call()

    with BlockTimer():
        os_api_call()

    logger.info("Performance Timing Completed.")
