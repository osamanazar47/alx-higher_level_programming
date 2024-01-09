#!/usr/bin/python3
"""Define a function save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """A function that writes an Object to a text file,
    using a JSON representation"""
    string = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(string)
