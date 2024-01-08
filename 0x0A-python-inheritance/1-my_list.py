#!/usr/bin/python3
"""Define a MyList class"""


class MyList(list):
    """Initializing a class MyList
    Usage:
       Inherits the list class and have a public instance method print_sorted
       print_sorted(self): prints the list but sorted in an ascending order
    """

    def print_sorted(self):
        """A public instance method that prints the list but sorted"""
        sorted_list = sorted(self)
        print(sorted_list)
