#!/usr/bin/python3
"""Define a print_square function"""


def print_square(size):
    """
    Initializing the function

    The function prints a square with the character #

    Args:
       size(int): the size length of the square

    Raises:
    TypeError: if size is not an integer
    ValueError: if size is less than 0
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
