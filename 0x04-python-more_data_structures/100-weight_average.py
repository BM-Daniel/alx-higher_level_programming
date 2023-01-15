#!/usr/bin/python3

def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    total, weight, average = 0, 0, 0
    for i in my_list:
        weight += i[1]
        total += (i[0] * i[1])

    return total / weight
