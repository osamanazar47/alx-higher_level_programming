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
    def matrix_divided(matrix, div):
        new_matrix = []
        if not isinstance(div, (int, float)):
            raise TypeError('div must be a number')
        if div == 0:
            raise ZeroDivisionError('division be zero')
        for i in range(len(matrix)):
            if i + 1 < len(matrix):
                if len(matrix[i]) != len(matrix[i + 1]):
                    raise TypeError('Each row of the matrix must have the same size')
            new_row = []
            for j in range(len(matrix[i])):
                if not isinstance(matrix[i][j], (int, float)):
                    raise TypeError('matrix must be a matrix (list of lists) of integers/floats')
                new_row.append(round(matrix[i][j] / div, 2))
            new_matrix.append(new_row)
        return new_matrix
