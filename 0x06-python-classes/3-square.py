#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Square - a class to define a square."""

    def __init__(self, size=0):
        """
        Initialize an instance of the square class

        Args:
             size(int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """
        an instance the returns the area of the square
        """
        return (self.__size * self.__size)
