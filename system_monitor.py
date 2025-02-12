import logging
import sys
import psutil
import json
from datetime import datetime
from models import SystemMetrics 
from config import Config

# Setup logging
handler = logging.StreamHandler(sys.stdout)
logging.basicConfig(level=logging.INFO, handlers=[handler, logging.FileHandler("app.log")])
logger = logging.getLogger(__name__)

def get_system_metrics():
    try:
        metrics = SystemMetrics(
            timestamp=datetime.now(),
            cpu_usage=psutil.cpu_percent(interval=1),
            ram_usage=psutil.virtual_memory().percent
        )
        return metrics
    except Exception as e:
        logger.error(f"Error reading system metrics: {e}")
        return None

if __name__ == "__main__":
    config = Config()
    app_config = config.get_app_config()

    logger.info(f"{app_config.greeting}.")
    if app_config.repeat_greeting:
        logger.info(f"{app_config.greeting} again")

    metrics = get_system_metrics()
    
    if metrics:
        metrics_json = metrics.json()
        logger.info(f"Serialized Metrics: {metrics_json}")

        deserialized_data = json.loads(metrics_json)
        logger.info(f"Deserialized Data - CPU Usage: {deserialized_data['cpu_usage']}%, RAM Usage: {deserialized_data['ram_usage']}%")

        exit_code = 0  
    else:
        exit_code = 1  
        
    sys.exit(exit_code)
