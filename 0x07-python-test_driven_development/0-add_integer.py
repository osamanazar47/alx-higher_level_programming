#!/usr/bin/python3
"""Define a function that returns the additio of two integers."""


def add_integer(a, b=98):
    """
    Return the addition of two integers

    float parameters are typecasted into integers
    Args:
      a(int or float): the first operand
      b(int or float): the second operand
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
