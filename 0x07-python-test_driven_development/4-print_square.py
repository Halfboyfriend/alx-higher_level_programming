#!/usr/bin/python3
"""
    Write a function that prints a square with
    the character #.
    Prototype: def print_square(size):
    size is the size length of the square
    size must be an integer, otherwise raise a TypeError
    exception with the message size must be an integer
    if size is less than 0, raise a ValueError exception
    with the message size must be >= 0
    if size is a float and is less than 0,
    raise a TypeError exception with the message size
    must be an integer
"""

def print_square(size):
    """Print a square size"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size, end="")
        print()
