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
