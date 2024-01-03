#!/usr/bin/python
"""Define say_my_name function"""


def say_my_name(first_name, last_name=""):
    """
    Initializing the function

    A function that prints "My name is <first name> <last name>"

    Args:
       first_name(str): the first name
       last_name(str): the last name

    Returns:
       No return

    Raises:
       TypeError: If first_name or last_name is not a string
    """
    if type(first_name) is not  str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
