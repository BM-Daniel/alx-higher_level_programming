#!/usr/bin/python3

def uppercase(str):
    ascii = 0

    for letter in str:
        ascii = ord(letter)
        if ascii > 96 and ascii < 123:
            ascii -= 32
        
        print("{}".format(chr(ascii)), end="")

    print()
