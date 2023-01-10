#!/usr/bin/python3
"""Write a function that writes a string to a text file (UTF8) and returns the number of characters written:"""


def write_file(filename="", text=""):
    """Function that writes into a file and create the file if not existing, returning the num of char."""
    with open(filename, mode="w", encoding="utf8") as file:
        return file.write(text)
