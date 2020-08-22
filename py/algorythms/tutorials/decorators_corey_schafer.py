"""
Corey Schafer Python tutorials
------------------------------
Python Decorators: https://www.youtube.com/watch?v=FsAPt_9Bf3U
"""
import logging
import time
from functools import wraps


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display_info(name: str, age: int) -> str:
    return f"display_info ran with arguments {name, age}"


class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self, *args, **kwargs):
        print(f"call method executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@decorator_class
def display_class(name: str, age: int) -> str:
    return f"display class decorator ran with arguments {name, age}"


def my_logger(orig_func):
    logging.basicConfig(filename=f"{orig_func.__name__}.log", level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(f"Ran with args: {args}, and kwargs: {kwargs}")
        return orig_func(*args, **kwargs)

    return wrapper


def my_timer(orig_func):
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{orig_func.__name__} ran in: {t2} sec")
        return result

    return wrapper


@my_logger
@my_timer
def display_info_logger_timer(name: str, age: int) -> str:
    time.sleep(1)
    return f"display_info_logger_timer ran with arguments ({name}, {age})"


if __name__ == "__main__":
    print(display_info("John", 25))
    print(display_class("John", 25))
    print(display_info_logger_timer("Tom", 22))
