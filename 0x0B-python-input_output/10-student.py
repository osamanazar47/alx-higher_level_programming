#!/usr/bin/python3
"""Creating a class Student"""


class Student:
    """
    Initializing a class Student
    with an __init__ method and to_json
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A method that returns the dic representation"""
        if attrs in None:
            return self.__dict__
        if not isinstance(attrs, list):
            raise TypeError('attrs must be a list')
        result = {}
        for element in attrs:
            if not isinstance(element, str):
                raise TypeError('Attribute names must be strings')
            if hasattr(self, element):
                result[element] = getattr(self, element)
            else:
                pass
        return result
