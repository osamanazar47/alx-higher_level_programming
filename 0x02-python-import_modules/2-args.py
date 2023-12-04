#!/usr/bin/python3
if __name__ == "__main__":
    print("{}".foramt(len(argv)), end='')
    if len(argv) == 1:
        print("argument" + ":" if len(argv) > 0 else ".")
    else:
        print("arguments" + ":" if len(argv) > 0 else ".")
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
