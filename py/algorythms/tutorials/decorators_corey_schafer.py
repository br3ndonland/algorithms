"""
Corey Schafer Python tutorials
------------------------------

Python Decorators: https://www.youtube.com/watch?v=FsAPt_9Bf3U
"""
import logging
import time
from functools import wraps
from typing import Any, Callable, Union


def decorator_function(original_function: Callable) -> Callable:
    def wrapper_function(*args: Union[int, str], **kwargs: Any) -> Callable:
        print(f"wrapper executed this before {original_function.__name__}")
        return original_function(*args, **kwargs)

    return wrapper_function


@decorator_function
def display_info(name: str, age: int) -> str:
    return f"display_info ran with arguments {name, age}"


class DecoratorClass:
    def __init__(self, original_function: Callable):
        self.original_function = original_function

    def __call__(self, *args: Union[int, str], **kwargs: Any) -> Callable:
        print(f"call method executed this before {self.original_function.__name__}")
        return self.original_function(*args, **kwargs)


@DecoratorClass
def display_class(*args: Union[int, str], **kwargs: Any) -> str:
    return f"display class decorator ran with arguments {args}"


def my_logger(original_function: Callable) -> Callable:
    logging.basicConfig(
        filename=f"{original_function.__name__}.log", level=logging.INFO
    )

    @wraps(original_function)
    def wrapper(*args: Union[int, str], **kwargs: Any) -> Callable:
        logging.info(f"Ran with args: {args}, and kwargs: {kwargs}")
        return original_function(*args, **kwargs)

    return wrapper


def my_timer(original_function: Callable) -> Callable:
    @wraps(original_function)
    def wrapper(*args: Union[int, str], **kwargs: Any) -> Callable:
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
