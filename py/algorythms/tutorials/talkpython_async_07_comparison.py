"""
Talk Python Training: Async Techniques and Examples in Python
---
Course: https://training.talkpython.fm/
Code: https://github.com/talkpython/async-techniques-python-course

Chapter 7: Multiprocessing

This module compares the processing speed of threading and multiprocessing.
"""
import datetime
import math
import multiprocessing
import threading


def do_math(start: int = 0, num: int = 10) -> int:
    """Do a sample math problem."""
    pos = start
    k_sq = 1000 * 1000
    avg: float = 0
    while pos < num:
        pos += 1
        val = math.sqrt((pos - k_sq) * (pos - k_sq))
        avg += val / num
    return int(avg)


def set_args(n: int, processor_count: int) -> tuple:
    """Set arguments to pass to target method."""
    return (30_000_000 * (n - 1) / processor_count, 30_000_000 * n / processor_count)


def run_threading(processor_count: int) -> None:
    """Do math with threads."""
    threads = [
        threading.Thread(target=do_math, args=set_args(n, processor_count), daemon=True)
        for n in range(1, processor_count + 1)
    ]
    for t in threads:
        t.start()
        t.join()
        print(t.name)


def run_multiprocessing(processor_count: int) -> None:
    """Do math with multiprocessing."""
    pool = multiprocessing.Pool()
    tasks = [
        pool.apply_async(do_math, set_args(n, processor_count))
        for n in range(1, processor_count + 1)
    ]
    pool.close()
    pool.join()
    for t in tasks:
        print(t.get())


def main(method: str = "multiprocessing") -> None:
    """Do math and print the result."""
    do_math(1)
    t0 = datetime.datetime.now()
    processor_count = multiprocessing.cpu_count()
    print(f"\nDoing math on {processor_count:,} processors with {method}.")
    if method == "multiprocessing":
        run_multiprocessing(processor_count)
    elif method == "threading":
        run_threading(processor_count)
    else:
        print("Method must be either multiprocessing or threading.")
    dt = datetime.datetime.now() - t0
    print(f"Done in {dt.total_seconds():,.2f} seconds.")


if __name__ == "__main__":
    main("threading")
    main("multiprocessing")
