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
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance
        with values from the dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
