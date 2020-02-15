import math as m
import random as r


def pi(inside, total):
    """
    Estimate Pi by throwing darts
    ---
    This was a whiteboard question in a software engineering job interview.
    I was asked to estimate Pi by randomly throwing "darts" at an imaginary
    dart board, represented by a circle inside a square.
    This solution uses Monte Carlo simulation.

    Key points:
    - The circle has radius 1 and area of Pi
    - The square has sides of length 2, and therefore area 4
    - The ratio of the areas of the circle to the square is Pi/4.
    """
    for i in range(0, total):
        x2 = r.random() ** 2
        y2 = r.random() ** 2
        if m.sqrt(x2 + y2) < 1.0:
            inside += 1
    pi = (float(inside) / total) * 4
    print(pi)


if __name__ == "__main__":
    inside = 0
    total = 10000
    pi(inside, total)
