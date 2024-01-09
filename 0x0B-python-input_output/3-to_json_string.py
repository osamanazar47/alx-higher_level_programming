#!/usr/bin/python3
"""Define a function to_json_string"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation of an object"""
    return json.dumps(my_obj)
