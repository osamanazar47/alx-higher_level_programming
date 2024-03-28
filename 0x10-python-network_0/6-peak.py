#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers, left=None, right=None):
    """A function that finds the peak in a list using divide and conquer."""
    if left is None:
        left = 0
    if right is None:
        right = len(list_of_integers) - 1

    if left == right:
        return list_of_integers[left]

    mid = (left + right) // 2

    if list_of_integers[mid] < list_of_integers[mid + 1]:
        # If the middle element is less than the next element, peak must be on the right side
        return find_peak(list_of_integers, mid + 1, right)
    else:
        # Otherwise, peak must be on the left side or at the middle element
        return find_peak(list_of_integers, left, mid)
