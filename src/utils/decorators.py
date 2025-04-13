"""
decorators.py

This module provides utility decorators for enhancing functions and methods within
the project. Included decorators manage retries, timeouts, and logging for function calls.
"""

import functools
import time
import logging

def retry(max_retries=3, delay=1, exception=Exception):
    """
    A decorator that retries a function call if an exception occurs.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exception as e:
                    retries += 1
                    logging.warning("Function %s failed on attempt %d/%d. Retrying...",
                                    func.__name__, retries, max_retries)
                    time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def timeit(func):
    """
    A decorator that logs the execution time of the decorated function.
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start_time
        logging.info("Function %s executed in %0.4f seconds", func.__name__, elapsed)
        return result
    return wrapper
