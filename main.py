import argparse
import socket
import logging
from server import start_server
from client import start_client  # Ensure correct import

# Setup logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def is_port_in_use(port):
    """Checks if a port is in use."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(("127.0.0.1", port)) == 0

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Protocol Client & Server Manager")
    parser.add_argument("-s", "--server", action="store_true", help="Run as server")
    parser.add_argument("-c", "--client", action="store_true", help="Run as client")
    parser.add_argument("-a", "--auto", action="store_true", help="Auto-detect and run server or client")
    parser.add_argument("--serverip", type=str, default="127.0.0.1", help="Override server IP")
    parser.add_argument("--port", type=int, default=54545, help="Override configured port")
    args = parser.parse_args()

    if args.server:
        logger.info("Starting in server mode...")
        start_server(host=args.serverip, port=args.port)
    elif args.client:
        logger.info("Starting in client mode...")
        start_client(serverip=args.serverip, port=args.port)  # Fix function call
    elif args.auto:
        if is_port_in_use(args.port):
            logger.info("Port in use, starting as client...")
            start_client(serverip=args.serverip, port=args.port)  # Fix function call
        else:
            logger.info("Port free, starting as server...")
            start_server(host=args.serverip, port=args.port)
    else:
        parser.print_help()
