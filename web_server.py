from flask import Flask, jsonify
import logging
from utils.timer import BlockTimer
from utils.data_snapshot import get_cached_metrics

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/hello")
def hello():
    logger.info("Received request for /hello")
    return jsonify({"message": "Hello World!"})

@app.route("/metrics")
def metrics():
    with BlockTimer():
        snapshot, response_time = get_cached_metrics()

    logger.info(f"Metrics retrieved at {response_time}, read at {snapshot.timestamp}")
    return jsonify({
        "read_timestamp": snapshot.timestamp.isoformat(),
        "response_timestamp": response_time.isoformat(),
        "cpu_usage": snapshot.cpu_usage,
        "ram_usage": snapshot.ram_usage
    })

if __name__ == "__main__":
    logger.info("Starting Web Server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
