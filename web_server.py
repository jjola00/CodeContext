from flask import Flask, jsonify
import logging
import time
from utils.timer import BlockTimer
from utils.data_snapshot import get_cached_metrics

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Simple /hello route
@app.route("/hello")
def hello():
    logger.info("Received request for /hello")
    return jsonify({"message": "Hello World!"})

# Updated /metrics route with caching & delays
@app.route("/metrics")
def metrics():
    with BlockTimer():
        time.sleep(5)  # Simulate slow response (>5s)
        snapshot, response_time = get_cached_metrics()

    logger.info("Metrics data retrieved")
    return jsonify({
        "read_timestamp": snapshot.timestamp.isoformat(),
        "response_timestamp": response_time.isoformat(),
        "cpu_usage": snapshot.cpu_usage,
        "ram_usage": snapshot.ram_usage
    })

if __name__ == "__main__":
    logger.info("Starting Web Server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
