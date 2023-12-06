#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    for key in a_dictionary:
        a_dictionary[key] = value
    else:
        add_value = {key : value}
        a_dictionary.update(add_value)
