from functools import wraps
import time

from testrail.exceptions import TooManyRequestsError


def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except TooManyRequestsError as e:
                time.sleep(e.delay)
    return wrapper
