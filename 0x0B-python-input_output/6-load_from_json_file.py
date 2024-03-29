#!/usr/bin/python3
"""Define a function load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file
    Args:
       filename: the name of the json file
    """
    with open(filename, 'r') as f:
        text = f.read()
        return json.loads(text)
