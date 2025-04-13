"""
sample_client.py

A sample UDP client to test the Scalable UDP Server.
This script sends a UDP packet to the server and prints the response.
"""

import socket
import json

def udp_client(server_ip, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        message = "Hello UDP Server"
        client_socket.sendto(message.encode(), (server_ip, server_port))
        response, _ = client_socket.recvfrom(1024)
        data = json.loads(response.decode())
        print("Received sensor data:")
        print(data)
    except Exception as e:
        print("Error in UDP client:", e)
    finally:
        client_socket.close()

if __name__ == "__main__":
    UDP_SERVER_IP = "127.0.0.1"
    UDP_SERVER_PORT = 4210
    udp_client(UDP_SERVER_IP, UDP_SERVER_PORT)
