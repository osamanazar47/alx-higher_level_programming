#!/usr/bin/python3
"""Define a read_file function"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it"""

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.read()
        print(lines)
