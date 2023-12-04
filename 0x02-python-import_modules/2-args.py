#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    print("{}".format(len(argv) - 1), end=' ')
    if len(argv) == 2:
        print("argument" + ":" if len(argv) > 0 else ".")
    else:
        print("arguments" + ":" if len(argv) > 0 else ".")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
