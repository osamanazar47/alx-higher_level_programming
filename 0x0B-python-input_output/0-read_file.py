#!/usr/bin/python3
"""Define a read_file function"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it"""

    with open(filename) as f:
        print(f.read())
