"""
metrics.py

A simple metrics collector for tracking the performance of the UDP server.
This module logs request counts and processing times and can be extended for real-time monitoring.
"""

import time
import logging

logger = logging.getLogger("MetricsService")

class MetricsCollector:
    def __init__(self):
        self.request_count = 0
        self.total_processing_time = 0.0
        logger.info("MetricsCollector initialized.")

    def record(self, processing_time):
        self.request_count += 1
        self.total_processing_time += processing_time
        logger.debug("Recorded processing time: %0.4f seconds", processing_time)

    def average_processing_time(self):
        if self.request_count == 0:
            return 0
        avg_time = self.total_processing_time / self.request_count
        logger.info("Average processing time: %0.4f seconds", avg_time)
        return avg_time

if __name__ == "__main__":
    collector = MetricsCollector()
    for i in range(5):
        collector.record(0.05 * (i + 1))
    print("Requests:", collector.request_count)
    print("Average Processing Time:", collector.average_processing_time())
