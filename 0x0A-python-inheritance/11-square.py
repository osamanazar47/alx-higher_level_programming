#!/usr/bin/python3
"""Define Square class that inherits from Rectangl"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """this is a Square class using Rectangle"""
    def __init__(self, size):
        """Initiaizing a new Square"""
        self.integer_validator('size', size)
        self.__size = size

    def area(self):
        """A method that returns the area of the square"""
        return self.__size * self.__size

    def __str__(self):
        string = "[" + str(self.__class__.__name__) + "] "
        string += self.__size + '/' + self.__size
        return string
