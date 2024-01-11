#!/usr/bin/python3
"""Defining Base class"""


class Base:
    """Base class with a private class attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """the constructor with a public instance attribute id"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
