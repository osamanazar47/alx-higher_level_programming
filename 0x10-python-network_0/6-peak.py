#!/usr/bin/python3
"""Finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """A function that finds the peak in a list using divide and conquer."""
    if len(list_of_integers) == 0:
        return None

    return find_peak_recursive(list_of_integers, 0, len(list_of_integers) - 1)


def find_peak_recursive(arr, left, right):
    """Recursive helper function to find peak in a list."""
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    if arr[mid] < arr[mid + 1]:
        # If the middle element is less than the next element, peak must be on the right side
        return find_peak_recursive(arr, mid + 1, right)
    else:
        # Otherwise, peak must be on the left side or at the middle element
        return find_peak_recursive(arr, left, mid)
