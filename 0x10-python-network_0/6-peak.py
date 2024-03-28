#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """ a function that finds the peak in a list"""

    if len(list_of_integers) == 0:
        return None

    peak = 0
    for i in list_of_integers:
        if i > peak:
            peak = i
    return peak
