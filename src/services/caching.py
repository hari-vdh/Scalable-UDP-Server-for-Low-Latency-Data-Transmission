"""
caching.py

Implements a simple in-memory caching mechanism for sensor data.
This service can be extended for distributed caching.
"""

import time
import logging

logger = logging.getLogger("CachingService")

class Cache:
    def __init__(self, ttl=60):
        self.cache = {}
        self.ttl = ttl  # Time to live in seconds
        logger.info("Cache initialized with TTL=%d seconds", ttl)

    def set(self, key, value):
        expiry = time.time() + self.ttl
        self.cache[key] = (value, expiry)
        logger.debug("Cache set: %s -> %s (expires at %s)", key, value, expiry)

    def get(self, key):
        if key in self.cache:
            value, expiry = self.cache[key]
            if time.time() < expiry:
                logger.debug("Cache hit for key: %s", key)
                return value
            else:
                logger.debug("Cache expired for key: %s", key)
                del self.cache[key]
        logger.debug("Cache miss for key: %s", key)
        return None

if __name__ == "__main__":
    cache = Cache(ttl=5)
    cache.set("sensor_data", {"humidity": 55, "temperature": 22})
    print("Cache retrieval:", cache.get("sensor_data"))
    time.sleep(6)
    print("Cache retrieval after expiration:", cache.get("sensor_data"))
