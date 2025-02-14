import socket
import logging

# Setup logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def start_client(serverip="127.0.0.1", port=54545):
    """Starts a TCP client that connects to the server."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((serverip, port))
        logger.info(f"Connected to server {serverip}:{port}")
        message = "Hello, Server!"
        client_socket.sendall(message.encode("utf-8"))
        logger.info(f"Sent: {message}")

if __name__ == "__main__":
    start_client()
