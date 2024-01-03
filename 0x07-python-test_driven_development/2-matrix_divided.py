#!/usr/bin/python3
"""Define a function matrix_divided."""


def matrix_divided(matrix, div):
    """
    Initializing the function

    matrix_divided - is a function that return a new matrix which contain all the elements of the main matrix divided by a number and rounded to a maximum of two decimal places

    Args:
       matrix(list of lists): the main matrix which contains elements of integers or floats
       div(int, float): the number by which we will divide the elements of the matrix by
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    msg_type = "matrix must be a matrix (list of lists) of integers/floats"
    if not matrix or not isinstance(matrix, list):
        raise TypeError(msg_type)
    len_row = 0
    msg_size = "Each row of the matrix must have the same size"
    for elements in matrix:
        if not elements or not isinstance(elements, list):
            raise TypeError(msg_type)
        if len_row != 0 and len(elements) != len_row:
            raise TypeError(msg_size)
        for num in elements:
            if not type(num) in (int, float):
                raise TypeError(msg_type)
        len_row = len(elements)
    m = list(map(lambda x: list(map(lambda y: round(y / div, 2), x)), matrix))
    return m
