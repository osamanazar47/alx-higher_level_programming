#!/usr/bin/python3
"""Define a function lookup(obj)"""


def lookup(obj):
    """
    A function that returns the list of available attributes 
    and methods of an object
    Args:
       obj(object): the object that we will return the list
       of all available attributes and methods of
    """
    return dir(obj)
