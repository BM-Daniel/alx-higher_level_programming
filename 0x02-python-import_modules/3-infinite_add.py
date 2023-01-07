#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    argv = sys.argv
    length = len(argv)
    add = 0

    for i in range(1, length):
        add += int(argv[i])

    print("{}".format(add))
