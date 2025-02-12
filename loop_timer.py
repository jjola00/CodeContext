import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def time_loop(iterations):
    start_time = time.time()
    for _ in range(iterations):
        pass
    elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
    logger.info(f"Loop Count: {iterations}, Elapsed Time: {elapsed_time:.6f} milliseconds")  # Updated to milliseconds

if __name__ == "__main__":
    logger.info("Starting Performance Timing...")

    for loop_size in [100, 10_000, 1_000_000]:
        time_loop(loop_size)

    logger.info("Performance Timing Completed.")
