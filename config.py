"""
config.py

Centralized configuration settings for sensor readings, UDP server, and advanced options.
"""

# Sensor Configuration
SENSOR_TYPE = "DHT22"         # Options: "DHT22" or "DHT11"
SENSOR_PIN = 4                # GPIO pin for sensor data
USE_SIMULATION = False        # Enable simulation mode for testing

# UDP Server Configuration
UDP_IP = "0.0.0.0"            # Listen on all network interfaces
UDP_PORT = 4210               # Port for UDP service

# Sensor Polling and Timeout
POLLING_INTERVAL = 2          # Seconds between sensor readings
RESPONSE_TIMEOUT = 5          # UDP socket timeout in seconds

# Advanced Options
DEBUG_MODE = True             # Enable verbose debug logging
MAX_RETRY_COUNT = 3           # Maximum sensor read retries

# Logging Settings
LOG_FILE = "server.log"       # Log file path
