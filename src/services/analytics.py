"""
analytics.py

Provides analytics functions that process historical sensor data.
This module is a stub for advanced analytical algorithms and statistical reporting.
"""

import logging
from collections import deque
import time

logger = logging.getLogger("AnalyticsService")

class AnalyticsService:
    def __init__(self, max_entries=100):
        self.temperature_history = deque(maxlen=max_entries)
        self.humidity_history = deque(maxlen=max_entries)
        logger.info("AnalyticsService initialized with max_entries=%d", max_entries)

    def record(self, data):
        """
        Record sensor data for analytical purposes.
        """
        self.temperature_history.append(data.get("temperature", 0))
        self.humidity_history.append(data.get("humidity", 0))
        logger.debug("Recorded data: %s", data)

    def average_temperature(self):
        if self.temperature_history:
            avg_temp = sum(self.temperature_history) / len(self.temperature_history)
            logger.info("Average temperature calculated: %s", avg_temp)
            return avg_temp
        return None

    def average_humidity(self):
        if self.humidity_history:
            avg_hum = sum(self.humidity_history) / len(self.humidity_history)
            logger.info("Average humidity calculated: %s", avg_hum)
            return avg_hum
        return None

if __name__ == "__main__":
    service = AnalyticsService()
    for i in range(1, 6):
        data = {"temperature": 20 + i, "humidity": 50 + i, "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")}
        service.record(data)
    print("Average Temperature:", service.average_temperature())
    print("Average Humidity:", service.average_humidity())
