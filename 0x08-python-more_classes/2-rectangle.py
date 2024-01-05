#!/usr/bin/python3
"""Define a Rectangle class"""


class Rectangle:
    """
    Initializing a Rectangle class

    Private instance attributes:
      width(int): the width of the rectangle
      height(int): the height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """the constructure for the Rectangle class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """A getter for the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """A setter for the width"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """A getter for the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """A setter for the height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (2 * (self.__width + self.__height))
