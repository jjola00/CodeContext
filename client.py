import socket
import logging
import time

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 54545

def start_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_HOST, SERVER_PORT))

        local_ip, local_port = client_socket.getsockname()
        remote_ip, remote_port = client_socket.getpeername()
        logger.info(f"Connected to Server {remote_ip}:{remote_port} from {local_ip}:{local_port}")

        for i in range(50):
            payload = f"Message {i+1}: " + "X" * (60 - len(f"Message {i+1}: "))  
            payload_bytes = payload.encode("utf-8")
            header = len(payload_bytes).to_bytes(4, byteorder="big") 
            message = header + payload_bytes  
            
            client_socket.sendall(message) 
            logger.info(f"Sent: {payload}")

            time.sleep(0.1) 

        input("Press Enter to exit...") 

if __name__ == "__main__":
    start_client()
