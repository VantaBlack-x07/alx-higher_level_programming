#!/usr/bin/python3
"""print square function"""


def print_square(size):
    """print a sqaure of #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
