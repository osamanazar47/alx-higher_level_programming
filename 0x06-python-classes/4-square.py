#!/usr/bin/python3
"""Define a Square class with getter and setter."""


class Square:
    """A square class."""

    def __init__(self, size=0):
        """
        Initialize a Square class

        Args:
        size(int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """get the current value of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """sets a new size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area of the square."""
        return (self.__size * self.__size)
