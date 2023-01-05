#!/usr/bin/python3

def islower(c):
    ascii = ord(c)

    if ascii > 96 and ascii < 123:
        return True
    else:
        return False
