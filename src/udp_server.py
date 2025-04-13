"""
udp_server.py

Creates a UDP server that listens for incoming client requests and responds with humidity and temperature data retrieved from the sensor.
The server uses multithreading to handle concurrent client requests. Extensive logging and error handling routines have been added.
"""

import socket
import json
import sys
import threading
import logging
from config import UDP_IP, UDP_PORT, RESPONSE_TIMEOUT, ENABLE_LOGGING, LOG_FILE, DEBUG_MODE
from sensor_reader import SensorReader

# Configure logging for the UDP server
logger = logging.getLogger("UDPServer")
logger.setLevel(logging.DEBUG if DEBUG_MODE else logging.INFO)
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler(LOG_FILE)
formatter = logging.Formatter('%(asctime)s - UDPServer - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def handle_client(sock, data, address, sensor_reader):
    """
    Handle an individual client's UDP request in a separate thread.
    This function reads the sensor data and replies with a JSON payload.
    """
    try:
        received_message = data.decode().strip()
        logger.info("Received request from %s: %s", address, received_message)
        sensor_data = sensor_reader.get_data()
        response = json.dumps(sensor_data)
        sock.sendto(response.encode(), address)
        logger.info("Sent response to %s: %s", address, response)
    except Exception as e:
        logger.exception("Error handling client %s: %s", address, e)

def monitor_performance(sensor_reader):
    """
    Periodically logs system performance and sensor data for monitoring.
    This function runs in its own thread.
    """
    while True:
        try:
            data = sensor_reader.get_data()
            logger.debug("Performance Monitor - Sensor Data: %s", data)
        except Exception as e:
            logger.error("Error in performance monitoring: %s", e)
        # Sleep between performance logs
        for _ in range(5):
            try:
                # This loop also checks for interruption
                threading.Event().wait(timeout=1)
            except KeyboardInterrupt:
                logger.info("Performance monitor interrupted.")
                break

def start_udp_server():
    """
    Start the UDP server to handle incoming UDP requests.
    This function initializes the socket, sensor reader, and monitoring thread.
    """
    # Create UDP socket
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((UDP_IP, UDP_PORT))
        server_socket.settimeout(RESPONSE_TIMEOUT)
        logger.info("UDP Server listening on %s:%s", UDP_IP, UDP_PORT)
    except Exception as e:
        logger.exception("Failed to create or bind UDP socket: %s", e)
        sys.exit(1)

    # Initialize sensor reader and start its thread
    sensor_reader = SensorReader()
    sensor_reader.start()

    # Start performance monitoring in a separate thread
    monitor_thread = threading.Thread(target=monitor_performance, args=(sensor_reader,), daemon=True)
    monitor_thread.start()
    logger.info("Performance monitoring thread started.")

    try:
        while True:
            try:
                data, address = server_socket.recvfrom(1024)
                # Log raw request received for debugging purposes
                logger.debug("Raw data received: %s from %s", data, address)
                # Create a new thread for each incoming client request
                client_thread = threading.Thread(
                    target=handle_client, args=(server_socket, data, address, sensor_reader))
                client_thread.start()
            except socket.timeout:
                logger.debug("Socket timeout waiting for client data. Continuing...")
                continue
            except Exception as e:
                logger.exception("Error receiving data: %s", e)
    except KeyboardInterrupt:
        logger.info("UDP server shutting down due to keyboard interrupt...")
    finally:
        sensor_reader.stop()
        server_socket.close()
        logger.info("UDP server closed. Exiting.")

def main():
    """
    Entry point for the UDP server application.
    Additional preliminary logging and self-test calls can be added here.
    """
    logger.info("Starting UDP server application.")
    start_udp_server()
    logger.info("UDP server application has stopped.")

# Extra function for future expansion, not currently used.
def advanced_request_handler():
    """
    Placeholder for an advanced UDP request handler that might implement
    additional protocol features, such as authentication or encryption.
    """
    pass

# for further networking features can be integrated.
#
# def udp_multicast_listener():
#     """
#     Example function to implement an UDP multicast listener in the future.
#     """
#     pass
#
# End placeholder for extended networking features.

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logger.exception("Fatal error in UDP server: %s", e)
        sys.exit(1)
