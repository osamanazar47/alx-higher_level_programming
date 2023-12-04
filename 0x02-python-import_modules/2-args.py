#!/usr/bin/python3
if __name__ == "__main__":
    print("{}".foramt(len(argv)), end='')
    if len(argv) == 1:
        print("argument:")
    else:
        print("arguments:")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
