# Talk Python Training: Async techniques

Course: [training.talkpython.fm](https://training.talkpython.fm/courses/explore_async_python/async-in-python-with-threading-and-multiprocessing)
GitHub: [talkpython/async-techniques-python-course](https://github.com/talkpython/async-techniques-python-course)

## Chapters

### Chapter 01: Welcome to the course

- Asynchronous programming is occurrence of events outside the main program flow
- End of Moore's law: power and heat problems led to multiple cores and prevent further improvements in speed. Concurrency allows us to take advantage of modern multi-core hardware.
- Start with `async` and `await` (asyncio).
- Three methods for implementing concurrency in Python
  1. Threads
  2. Processes
  3. Asyncio
- Two types of parallelism (primarily because of the [Global Interpreter Lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock) (GIL))
  1. Threaded
  2. Process-based (useful for computational work)
- Execution pools allow us to switch between the two types of parallelism.

### Chapter 02: Setup and following along

- Michael uses Camtasia for screen recording.
- It looks like Pycharm has a screencasting feature that displays keyboard shortcuts as they are used. VSCode has a similar feature.

### Chapter 03: Why async?

#### Speed

- End of Moore's law:
  - Jeffrey Funk presentation on slideshare (slideshare.net/Funk98)
  - Power and heat problems led to multiple cores and prevent further improvements in speed.
  - Concurrency allows us to take advantage of modern multi-core hardware.
- Michael runs [`glances`](https://nicolargo.github.io/glances/) on macOS for system monitoring. [Doesn't work on Apple Silicon](https://github.com/nicolargo/glances/issues/1769) yet (I tried installing with pipx, and even running with `sudo`).
- There's an upper bound for speed improvement.

#### Scaleability

- Scaleability for web apps mainly refers to the total number of requests the system can handle.
- Web API calls involve a lot of waiting. Synchronous code blocks while waiting.
- Asynchronous code allows our application to be more productive while waiting.

#### Python async landscape

- **Do more at once**
  - `asyncio`
  - `threading`
- **Do things faster**
  - `multiprocessing`
  - Cython
- **Do these easier**
  - trio
  - unsync

#### Why threads don't perform in Python

- GIL = "[Global Interpreter Lock](https://docs.python.org/3/glossary.html#term-global-interpreter-lock)". Only one step of execution can run at a time.
- GIL is a memory management feature. Reference counting is simpler and faster.
- The GIL optimizes serial execution of Python code, which is the predominant use case.

### Chapter 04: Async and await with asyncio

- I/O-driven concurrency can simulate concurrency, but without parallel threads. It can break a single thread into multiple tasks, or processes, and denote where the program is awaiting on a task.
- Asyncio is "cooperative" I/O-driven concurrency.
- A "coroutine" is like a restartable function. [A generator is a kind of coroutine](https://www.python.org/dev/peps/pep-0342/).
- Generators can pause execution and continue running.
- Producer-consumer app

  - Michael codes a simple API. The producer generates data, the consumer processes it.
  - Michael then revises the method to generate and process data asynchronously with [`asyncio`](https://docs.python.org/3/library/asyncio.html). The program runs faster.

    ```py
    loop = asyncio.get_event_loop()

    data = asyncio.Queue()

    task1 = loop.create_task(generate_data(20, data))
    task2 = loop.create_task(generate_data(20, data))
    task3 = loop.create_task(process_data(40, data))

    final_task = asyncio.gather(task1, task2, task3)
    loop.run_until_complete(final_task)
    ```

- Anatomy of an async method
  - `async def` to denote that the method is async
  - `await` asynchronous calls within the method
- Web scraping
  - Michael writes a simple web scraping program with Requests and Beautiful Soup.
  - Michael then speeds up the program by using [AIOHTTP](https://docs.aiohttp.org/en/stable/) instead of Requests.
- Other async-enabled libraries
  - [Tinche/aiofiles](https://github.com/Tinche/aiofiles) (files)
  - [Scille/umongo](https://github.com/Scille/umongo) (MongoDB)
  - [MagicStack/asyncpg](https://github.com/MagicStack/asyncpg) (PostgreSQL)
  - [jonathanslenders/asyncio-redis](https://github.com/jonathanslenders/asyncio-redis) (Redis, also see [aio-libs/aioredis](https://github.com/aio-libs/aioredis) and [samuelcolvin/arq](https://github.com/samuelcolvin/arq))

### Chapter 05: Threads

- Threads have been available in Python for a long time.
- Threads accomplish a similar goal as `asyncio`: doing more at once.
- Threads enable parallel programming.
- Choosing between threads and `asyncio`: `asyncio` has a simpler API
- Python has a [standard library `threading` module](https://docs.python.org/3/library/threading.html) for working with threads.
- By default, threads are "foreground" threads, meaning that they will continue running, even if the Python program itself is no longer running. Background threads can be enabled with `daemon=True`.

Basic `threading` program: `talkpython_async_05_threading.py`

```py
"""
Talk Python Training: Async Techniques and Examples in Python
---
Course: https://training.talkpython.fm/
Code: https://github.com/talkpython/async-techniques-python-course

Chapter 5: Threading

This is a simple demonstration of how background, or "daemon," threads allow
other work to continue in the foreground.
"""
import threading
import time


def generate_data(name: str, num: int) -> None:
    """Generate data for thread. Your normal synchronous code goes here."""
    for n in range(num):
        print(f"Hello {name}! This is greeting number {n + 1}.")
        time.sleep(0.5)


def main() -> None:
    """Run a background thread, do other work, and wait for completion."""
    # Create thread
    thread = threading.Thread(target=generate_data, args=("You", 5), daemon=True)
    # Start thread
    thread.start()
    # Do other work while thread is running
    print("I'm doing other work!")
    # Wait for completion
    thread.join(timeout=5 * 0.5)
    # Finish up
    print("Done.")


if __name__ == "__main__":
    main()

```

- _How do I pass in keyword arguments?_ -> Use the `kwargs={}` argument to pass `kwargs`. Michael didn't explain this, but I looked it up later in the [threading docs](https://docs.python.org/3/library/threading.html).
- Instantiate threads in a list to work with more than one at a time.
- Attempting to leverage multiple cores with threads: Michael sets up a sample math function. "It doesn't really matter what math it's doing, just that it is doing math is pretty interesting."
- Caveat: The GIL can only operate on one instruction at a time, so **threaded work can't be spread across multiple CPU cores**. To spread computations among multiple CPU cores, use `multiprocessing` or Cython _(the "do things faster" part of the async landscape)_.

### Chapter 06: Thread safety

- **Threads require safety measures.** Threading errors are difficult to troubleshoot. They are often referred to as "Heisenbugs." There's always uncertainty.
- In a Python program, data may be in temporarily invalid states while they are being modified by the program. If multiple threads reference or change the same data structures while the states are temporarily invalid, errors can occur.
- Michael demonstrates various thread locking methods to improve thread safety.
  - Always use `threading.RLock()` over `threading.Lock()` to allow re-entry.
  - Use a `with` context manager to contain potentially unsafe operations.
- When attempting to improve thread safety, it is possible to create a deadlock, in which the threads can't finish and release. It's very important to start and release locks in the proper order.

### Chapter 07: Leveraging CPU cores with `multiprocessing`

- This chapter focuses on the "do things faster" part of the async landscape.
- From the [`multiprocessing` docs](https://docs.python.org/3/library/multiprocessing.html):
  > The `multiprocessing` package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, the `multiprocessing` module allows the programmer to fully leverage multiple processors on a given machine.
- `multiprocessing` sidesteps the GIL by creating subprocesses, and giving each subprocess its own GIL.
- Parallelizing code with `multiprocessing`:
  - Create a new `multiprocessing.pool.Pool()` instance
  - Start the work with `pool.apply_async()`
  - Finish the work with `pool.close()` and then `pool.join()`.
- Return values can be accessed using `pool.apply_async().get()` if needed.

#### Additional notes on `multiprocessing`

- The ["Sharing state between processes" section of the `multiprocessing` docs](https://docs.python.org/3/library/multiprocessing.html#sharing-state-between-processes) recommends avoiding shared state in general, as attempts to access data that are in temporarily invalid states can lead to errors. Michael warns of the same limitation with threads in the thread safety section. However, there are some methods for using shared state with `multiprocessing`.
- I'm not sure, but the docs seem to imply that `multiprocessing` doesn't explicitly distribute workers evenly among CPU cores. This is the job of the operating system.

#### Gunicorn and Uvicorn

- Gunicorn doesn't directly use `multiprocessing`, nor does it directly distribute workers evenly among CPU cores. See the [FAQ](https://docs.gunicorn.org/en/latest/faq.html), and [this section of the design docs](https://docs.gunicorn.org/en/latest/design.html#how-many-workers):
  > Gunicorn relies on the operating system to provide all of the load balancing when handling requests. Generally we recommend `(2 x $num_cores) + 1` as the number of workers to start off with. While not overly scientific, the formula is based on the assumption that for a given core, one worker will be reading or writing from the socket while the other worker is processing a request.
- Uvicorn does implement subprocesses with `multiprocessing` in [uvicorn/subprocess.py](https://github.com/encode/uvicorn/blob/a504c56963fb0d4c9add33fe3d1cb3fc25d82fdb/uvicorn/subprocess.py).
- Uvicorn also implements a Gunicorn worker in [uvicorn/workers.py](https://github.com/encode/uvicorn/blob/a504c56963fb0d4c9add33fe3d1cb3fc25d82fdb/uvicorn/workers.py). Gunicorn handles the main process, and each "worker" process runs the Uvicorn worker.

#### Comparing `threading` and `multiprocessing`

Michael uses the math function from the end of chapter 5 ("Attempting to leverage multiple cores with threads") to compare `threading` and `multiprocessing`.

I wrote my own module to compare `threading` and `multiprocessing`, based on Michael's module `compute_multiprocessing.py`, but with a more direct comparison between the two (although there's no built-in method for getting the return value with `threading`). On my Apple Silicon M1 Mac Mini with 8 cores and Python 3.8.2, the module runs about four times faster with `multiprocessing` than with `threading`.

Module: `talkpython_async_07_comparison.py`

```py
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

```

Results on Apple Silicon M1 Mac Mini:

```text
Doing math on 8 processors with threading.
Thread-1
Thread-2
Thread-3
Thread-4
Thread-5
Thread-6
Thread-7
Thread-8
Done in 4.10 seconds.

Doing math on 8 processors with multiprocessing.
1141666
2312500
2791666
3031250
3175000
3270833
3339285
3390625
Done in 0.91 seconds.
```

Results on [DigitalOcean](https://www.digitalocean.com/) droplet (Ubuntu 20.04 LTS x64, 2 vCPU, 4 GB RAM):

```text
Doing math on 2 processors with threading.
Thread-1
Thread-2
Done in 10.07 seconds.

Doing math on 2 processors with multiprocessing.
6566667
10750000
Done in 5.29 seconds.
```

### Chapter 08: Common APIs with execution pools

- Michael modifies the web scraping code with the [`concurrent.futures` module](https://docs.python.org/3/library/concurrent.futures.html) to compare `threading` and `multiprocessing`.
- Running with threads: `concurrent.futures.thread`
- Running with processes: `concurrent.futures.process`
- Another approach (developed after Michael recorded the course) is to use [HTTPX](https://www.python-httpx.org/) instead of Requests.

### Chapter 09: Built on asyncio

- Michael discusses `unsync` and `trio` _(the "do these easier" part of the async landscape)_.
- There are several limitations of standard library tools that justify the need for easier async programming:
  - Executing an async function outside an existing event loop is problematic
  - [`asyncio.Future`](https://docs.python.org/3/library/asyncio-future.html#future-object) is not thread-safe.
  - [`concurrent.Future`](https://docs.python.org/3/library/concurrent.futures.html#future-objects) can't be directly awaited.
  - `Future.result()` (either from `asyncio` or `concurrent.futures`) blocks, even if within an event loop.
  - `asyncio.Future.result()` will throw an exception if the future is not done.
  - Async functions execute in the `asyncio` loop, not in threads or processes.
  - Cancellation and timeouts are complicated.
  - Thread local storage _(like a global variable, but each thread has its own copy)_ doesn't work for `asyncio`.
  - Testing concurrent code is complicated.
- [`unsync`](https://asherman.io/projects/unsync.html)
  - Michael thinks C# has implemented async and await very well.
  - `unsync` implements an async API inspired by C#.
  - Michael demonstrates the progression from synchronous code to asynchronous code with `unsync`.
  - `unsync` enables mixed-mode parallelism: some code can run synchronously, some asynchronously, some in threads, some in processes.
- [trio](https://trio.readthedocs.io/en/stable/)
  - Trio is a Python library that simplifies async/await and enables parallelized I/O. It therefore helps with both the "do more at once" and the "do things faster" parts of the async landscape discussed in this course.
  - I particularly appreciate the helpful, friendly [documentation](https://trio.readthedocs.io/en/stable/), and extensive testing resources. Trio offers a [`trio.testing` module](https://trio.readthedocs.io/en/stable/reference-testing.html), and a [pytest plugin](https://pytest-trio.readthedocs.io/en/stable/).
  - Trio uses an async context manager called a [nursery](https://trio.readthedocs.io/en/stable/reference-core.html#tasks-let-you-do-multiple-things-at-once).
  - Trio also enables cancellation.

### Chapter 10: Asyncio-based web frameworks

- [Quart](https://gitlab.com/pgjones/quart) is an async implementation of [Flask](https://flask.palletsprojects.com/en/1.1.x/). Michael mentions the interview with Flask maintainer David Lord on [Talk Python to Me episode 177](https://talkpython.fm/episodes/show/177/flask-goes-1.0).
- Michael converts a web API from Flask to Quart. When running the app with [Hypercorn](https://gitlab.com/pgjones/hypercorn), and benchmarking with [`wrk`](https://github.com/wg/wrk), Quart provides substantial performance improvements.

### Chapter 11: Parallelism in C with Cython

- Cython relates to the "do things faster" part of the async landscape.
- Python has great [built-in support for C](https://docs.python.org/3/extending/extending.html).
- [Cython](https://cython.org/) is a third-party static compiler for Python. To use it, you will need to `pip install cython`, use `cimport` instead of `import`, use Cython's type-annotations, and compile ("cythonize") the code. Cython can increase speed, especially for specific computationally-intensive parts of the program.
- Cython has some methods for escaping the GIL to increase speed even further.
  - `with nogil` context manager
  - All code inside the context must be Cython
  - Michael speeds up the code 5600x using the `nogil` strategy. However, there are additional memory management considerations, such as "overflowing" integers. After correcting for integer overflow, it's 56x faster.

### Chapter 12: Course conclusion and review

- Really helpful course.
- It would have been great to have an overview of [ASGI](https://asgi.readthedocs.io/en/latest/) as well.
