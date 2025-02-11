import logging
import sys
import psutil
import os  # Import os module for reading environment variables
from config import Config

class ColoredFormatter(logging.Formatter):
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'

    def format(self, record):
        if record.levelno == logging.INFO:
            record.msg = f"{self.GREEN}{record.msg}{self.ENDC}"
        elif record.levelno == logging.ERROR:
            record.msg = f"{self.RED}{record.msg}{self.ENDC}"
        return super().format(record)

# Configure logging with the custom formatter
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s'))

logging.basicConfig(
    level=logging.INFO,
    handlers=[
        handler,  # Use the custom handler for console output
        logging.FileHandler("app.log")  # Log to a file
    ]
)

logger = logging.getLogger(__name__)  # Create a logger

def read_system_metrics():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)  # CPU usage in percentage
        ram_usage = psutil.virtual_memory().percent  # RAM usage in percentage

        logger.info(f"CPU Usage: {cpu_usage}%")
        logger.info(f"RAM Usage: {ram_usage}%")

        return 0  # Success
    except Exception as e:
        logger.error(f"Error reading system metrics: {e}")
        return 1  # Failure

if __name__ == "__main__":
    config = Config()
    app_config = config.get_app_config()

    # Log greeting
    logger.info(f"{app_config.greeting}.")
    if app_config.repeat_greeting:
        logger.info(f"{app_config.greeting} again")

    # Read and log environment variables
    exit_code = read_system_metrics()

    # Exit the application with the appropriate exit code
    sys.exit(exit_code)
