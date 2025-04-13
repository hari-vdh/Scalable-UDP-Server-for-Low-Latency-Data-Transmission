"""
exceptions.py

Defines custom exception classes
These are used to provide more meaningful error messages in different modules.
"""

class SensorReadError(Exception):
    """Exception raised when a sensor reading fails."""
    def __init__(self, message="Sensor reading failed after maximum retries"):
        super().__init__(message)

class UDPServerError(Exception):
    """Exception raised for errors in the UDP server."""
    def __init__(self, message="An error occurred in the UDP server"):
        super().__init__(message)

class ConfigurationError(Exception):
    """Raised when there is an error in configuration or missing environment settings."""
    def __init__(self, message="Configuration setting error"):
        super().__init__(message)
