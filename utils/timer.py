import time
import logging

logger = logging.getLogger(__name__)

class BlockTimer:
    """RAII-style performance timer using time.perf_counter()"""
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        elapsed_time = (time.perf_counter() - self.start_time) * 1000  # Convert to milliseconds
        logger.info(f"Elapsed Time: {elapsed_time:.6f} milliseconds")