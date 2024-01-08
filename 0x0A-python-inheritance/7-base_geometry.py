#!/usr/bin/python3
"""Define a class BaseGeometry"""


class BaseGeometry:
    """
    Initializing a class BasGeometry
    with a new public instance method integer_validator that validates value
     Raises:
        TypeError: if value is not an integer
        ValueError: if value is less or equal to 0
    """
    def area(self):
        """
        A function raises an Exception with the message
        area() is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """A function that validates a value"""
        if not isinstance(value, int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
