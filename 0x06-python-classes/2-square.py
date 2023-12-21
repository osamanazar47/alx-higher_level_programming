#!/usr/bin/python3

"""Define a class by the name of Square."""


class Square:
    """representatio of a square"""

    def __init__(self, size=0):
        """
        begenning of a new square

        Args:
           size(int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
