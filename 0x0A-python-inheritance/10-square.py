#!/usr/bin/python3
"""Define Square class that inherits from Rectangle"""
Rectangle = __import__('10-square').Square


class Square(Rectangle):
    """this is a Square class using Rectangle"""
    def __init__(self, size):
        """Initiaizing a new Square"""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """A method that returns the area of the square"""
        return self.__size * self.__size
