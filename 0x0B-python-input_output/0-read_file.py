#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file."""
    with open(filename, encoding="utf8") as file:
        print(file.read(), end="")
