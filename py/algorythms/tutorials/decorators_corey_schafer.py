"""
Corey Schafer Python tutorials
------------------------------
Python Decorators: https://www.youtube.com/watch?v=FsAPt_9Bf3U
"""
import logging
import time
from functools import wraps
from typing import Any, Union


def decorator_function(original_function: Any) -> Any:
    def wrapper_function(*args: tuple, **kwargs: dict) -> Any:
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display_info(name: str, age: int) -> str:
    return f"display_info ran with arguments {name, age}"


class DecoratorClass:
    def __init__(self, original_function: Any):
        self.original_function = original_function

    def __call__(self, *args: Union[int, str, tuple], **kwargs: dict) -> Any:
        print(f"call method executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_class(*args: tuple, **kwargs: dict) -> str:
    return f"display class decorator ran with arguments {args}"


def my_logger(original_function: Any) -> Any:
    logging.basicConfig(
        filename=f"{original_function.__name__}.log", level=logging.INFO
    )

    @wraps(original_function)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        logging.info(f"Ran with args: {args}, and kwargs: {kwargs}")
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function: Any) -> Any:
    @wraps(original_function)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        t1 = time.time()
        result = original_function(*args, **kwargs)
        t2 = time.time() - t1
        print(f"{original_function.__name__} ran in: {t2} sec")
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
