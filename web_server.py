from flask import Flask, jsonify
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route("/hello")
def hello():
    logger.info("Received request for /hello")
    return jsonify({"message": "Hello World!"})

if __name__ == "__main__":
    logger.info("Starting Web Server...")
    app.run(host="0.0.0.0", port=5000, debug=True)
