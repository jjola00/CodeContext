import time
import logging
import ctypes 

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

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