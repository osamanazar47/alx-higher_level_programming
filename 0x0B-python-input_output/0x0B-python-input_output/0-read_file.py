#!/usr/bin/python3
"""Define a function read_file"""


def read_file(filename=''):
    """A function that that reads a text file and prints it"""

    with open(filename) as f:
        print(f.read())
