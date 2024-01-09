#!/usr/bin/python3
"""Define a function write_file"""


def write_file(filename="", text=""):
    """
    A function that writes a string to a text file
    Returns: the number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        print(f.write(text), end='')
