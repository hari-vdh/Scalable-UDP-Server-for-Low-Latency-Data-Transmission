"""
logger.py

Custom logger configuration for the Scalable UDP Server project.
This module sets up advanced logging features, including logging to both console
and file with configurable log levels and formatting.
"""

import logging
from config import LOG_FILE, DEBUG_MODE

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if DEBUG_MODE else logging.INFO)

    # Create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG if DEBUG_MODE else logging.INFO)

    # Create file handler
    fh = logging.FileHandler(LOG_FILE)
    fh.setLevel(logging.DEBUG if DEBUG_MODE else logging.INFO)

    # Create formatter and add it to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    fh.setFormatter(formatter)

    # Add handlers to logger if they are not already added
    if not logger.handlers:
        logger.addHandler(ch)
        logger.addHandler(fh)

    return logger

# Example usage:
if __name__ == "__main__":
    log = setup_logger("TestLogger")
    log.debug("Debug message from TestLogger")
    log.info("Info message from TestLogger")
    log.warning("Warning message from TestLogger")
    log.error("Error message from TestLogger")
    log.critical("Critical message from TestLogger")
