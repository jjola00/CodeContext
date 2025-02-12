import socket
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

HOST = "0.0.0.0"
PORT = 54545

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)
        logger.info(f"Server listening on port {PORT}")

        while True:
            conn, addr = server_socket.accept()
            logger.info(f"Connected by {addr}")

            buffer = b""

            while True:
                data = conn.recv(50)
                if not data:
                    break

                buffer += data

                while len(buffer) >= 4:
                    msg_length = int.from_bytes(buffer[:4], byteorder="big")
                    if len(buffer) >= 4 + msg_length:
                        message = buffer[4:4 + msg_length].decode("utf-8")
                        logger.info(f"Received Complete Payload: {message}")
                        buffer = buffer[4 + msg_length:]
                    else:
                        break

            conn.close()
            logger.info(f"Connection closed with {addr}")

if __name__ == "__main__":
    start_server()
