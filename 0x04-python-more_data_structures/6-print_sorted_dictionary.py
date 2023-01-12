#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    a_keys = list(a_dictionary.keys())
    a_keys.sort()

    [print("{}: {}".format(i, a_dictionary[i])) for i in a_keys]
