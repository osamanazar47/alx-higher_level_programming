#!/usr/bin/python3
"""Define Square class that inherits from Rectangle"""


class Square(Rectangle):
    """this is a Square class using Rectangle"""
    def __init__(self, size):
        """Initiaizing a new Square"""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
