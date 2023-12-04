#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{}".format(len(argv) - 1), end=' ')
    if len(argv) == 2:
        print("argument", end='')
    else:
        print("arguments", end='')
    if len(argv) == 1:
        print(".")
    else:
        print(":")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
