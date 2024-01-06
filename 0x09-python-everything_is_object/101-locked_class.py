#!/usr/bin/python3
"""Define a class LockedClass"""


class LockedClass:
    """A class that allows instances to have only attribute named first_name"""
    __slots__ = ["first_name"]
