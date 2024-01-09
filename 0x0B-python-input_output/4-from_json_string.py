#!/usr/bin/python3
"""Define a function from_json_string"""
import json


def from_json_string(my_str):
    """A function that returns an object represented by JSON string"""
    return json.loads(my_str)
