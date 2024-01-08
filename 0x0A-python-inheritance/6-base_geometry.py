#!/usr/bin/python3
"""Define BaseGeometry class"""


class BaseGeometry:
    """
    Initializing a class BaseGeometry with a public instance method area
    Raises:
         an Exception with the message area() is not implemented
    """
    def area(self):
        raise Exception('area() is not implemented')
