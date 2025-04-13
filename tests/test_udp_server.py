import unittest
import socket
import json
import threading
import time
from src.udp_server import start_udp_server
from config import UDP_IP, UDP_PORT

class TestUDPServer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Start the UDP server in a separate thread for testing
        cls.server_thread = threading.Thread(target=start_udp_server, daemon=True)
        cls.server_thread.start()
        time.sleep(3)  # Allow time for the server to start

    def test_udp_response(self):
        # Create a UDP client to send a request to the server
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(5)
        try:
            message = "Test request"
            client_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))
            data, _ = client_socket.recvfrom(1024)
            response = json.loads(data.decode())
            self.assertIn("timestamp", response)
        except Exception as e:
            self.fail(f"UDP server response test failed: {e}")
        finally:
            client_socket.close()

if __name__ == "__main__":
    unittest.main()
