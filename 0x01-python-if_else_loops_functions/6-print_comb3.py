#!/usr/bin/python3
for i in range(0, 9):
    for n in range(i + 1, 10):
        if i == 8 and n == 9:
            print("{}{}".format(i, n))
            break
        print("{}{}".format(i, n), end=', ')
