#!/usr/bin/python3
"""
Write a function that finds a peak in a list of unsorted integers.
"""


def find_peak(list_of_integers):
    """
    Function to find peak
    """

    if list_of_integers == []:
        return None

    length = len(list_of_integers)

    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    midValue = int(length / 2)
    peakValue = list_of_integers[midValue]

    if (peakValue > list_of_integers[midValue - 1]) and \
       (peakValue > list_of_integers[midValue + 1]):
        return peakValue
    elif peakValue < list_of_integers[midValue - 1]:
        return find_peak(list_of_integers[:midValue])
    else:
        return find_peak(list_of_integers[midValue + 1:])
