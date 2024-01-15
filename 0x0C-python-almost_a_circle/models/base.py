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
        """Return the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            If json_string is None or empty - an empty list.
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None:
            json_string = []
            return json_string
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instantiated from a file of JSON strings.

        Reads from `<cls.__name__>.json`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        name = str(cls.__name__) + ".json"
        try:
            with open(name, "r") as f:
                list_dicts = Base.from_json_string(f.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            empty_list = []
            return empty_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """A method that saves to file csv with it's format"""
        name = "{}.csv".format(cls.__name__)
        with open(name, "w") as file:
            for obj in list_objs:
                if isinstance(obj, Rectangle):
                    line = "{},{},{},{},{}".format(obj.id, obj.width, obj.height, obj.x, obj.y)
                elif isinstance(obj, Square):
                    line = "{},{},{},{}".format(obj.id, obj.size, obj.x, obj.y)

                file.write(line + "\n")

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        name = "{}.csv".format(cls.__name__)
        objects = []

        with open(name, "r") as f:
            for line in f:
                values = line.strip().split(",")
                if cls.__name__ == "Rectangle":
                    obj = cls(
                        id=int(values[0]),
                        width=int(values[1]),
                        height=int(values[2]),
                        x=int(values[3]),
                        y=int(values[4])
                    )
                elif cls.__name__ == "Square":
                    obj = cls(
                        id=int(values[0]),
                        size=int(values[1]),
                        x=int(values[2]),
                        y=int(values[3])
                    )
                objects.append(obj)

        return objects
