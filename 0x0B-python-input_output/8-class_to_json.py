#!/usr/bin/python3
"""Define a function class_to_join""


def class_to_json(obj):
    """Returns the dictionary description for an object"""
    return obj.__dict__
