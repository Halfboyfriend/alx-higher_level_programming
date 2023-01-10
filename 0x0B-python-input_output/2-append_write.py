#!/usr/bin/python3
"""
Write a function that appends a string at the end of a text file (UTF8) and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """function that appends to a string."""
    with open(filename, mode="a", encoding="utf8") as file:
        return file.write(text)
