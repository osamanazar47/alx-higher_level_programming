#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    ftuple = tuple_a + (0, 0)
    stuple = tuple_b + (0, 0)
    new_tuple = ftuple[0] + stuple[0], ftuple[1] + stuple[1]
    return new_tuple
