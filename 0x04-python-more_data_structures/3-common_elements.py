#!/usr/bin/python3

def common_elements(set_1, set_2):
    elements = set()

    for element in set_1:
        for element2 in set_2:
            if element == element2:
                elements.add(element)

    return elements
