#!/usr/bin/python3
def islower(c):
    if ord(c) in range(97, 123):
        print("{} => lower".format(c))
        return True
    else:
        print("{} => upper".format(c))
        return False
