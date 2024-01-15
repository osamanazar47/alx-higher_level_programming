#!/usr/bin/python3
"""Defining Base class"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dictionaries.

        Args:
            list_dictionaries(list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        json_rep = cls.to_json_string([obj.to_dictionary() for obj in list_objs])
        name = cls.__name__
        filename = "{}.json".format(name)
        with open(filename, "w") as f:
            f.write(json_rep)
    
    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            json_string = []
            return json_string
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
        return dummy
