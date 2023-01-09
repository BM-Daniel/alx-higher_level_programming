#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    verify = []

    for i in my_list:
        if i % 2 == 0:
            verify.append(True)
        else:
            verify.append(False)

    return verify
