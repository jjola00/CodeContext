import socket
import logging

# Setup logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def start_server(host="0.0.0.0", port=54545):
    """Starts a TCP server listening on the specified port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(5)
        logger.info(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            logger.info(f"Connected by {addr}")
            data = conn.recv(1024)
            if not data:
                break
            logger.info(f"Received: {data.decode('utf-8')}")
            conn.close()
            logger.info(f"Connection closed with {addr}")

if __name__ == "__main__":
    start_server()
