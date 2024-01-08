#!/usr/bin/python3
"""Define a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initializng a class Rectangle"""

    def __init__(self, width, height):
        """A new Rectangle"""
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        """ A method that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """returns an info about the rectangle"""
        return "[{}] {}/{}"format(str(self.__class__.__name__),str( self.__width), str(self.__height))
