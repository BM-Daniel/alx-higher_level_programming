#!/usr/bin/python3

def best_score(a_dictionary):

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    biggest = 0
    biggest_key = ""
    for key in a_dictionary:
        if a_dictionary[key] > biggest:
            biggest = a_dictionary[key]
            biggest_key = key

    return biggest_key
