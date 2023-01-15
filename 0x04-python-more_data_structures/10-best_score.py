#!/usr/bin/python3

def best_score(a_dictionary):

    if a_dictionary is None:
        return None

    biggest = 0
    biggest_key = ""
    for key in a_dictionary:
        if a_dictionary[key] > biggest:
            biggest = a_dictionary[key]
            biggest_key = key

    return biggest_key
