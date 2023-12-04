#!/usr/bin/python3
def max_integer(my_list=[]):
    n = 0
    for i in range(len(my_list)):
        if n < my_list[i]:
            n = my_list[i]
    return n
