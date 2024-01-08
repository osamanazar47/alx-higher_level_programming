#!/usr/bin/python3
"""Define is_same_class function"""


def is_same_class(obj, a_class):
    """
    A function that that returns True if the object is exactly
    an instance of the specified class ; otherwise False
    """
    if type(obj) is a_class:
        return True
    return False
