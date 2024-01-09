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

    def to_json(self):
        """A method that returns the dic representation"""
        return self.__dict__
