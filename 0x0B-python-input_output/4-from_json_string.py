#!/usr/bin/python3

"""
Write a function that returns an object (Python data structure) represented
by a JSON string
"""

import json


def from_json_string(my_str):
    """ Convert object to string - json """

    return json.loads(my_str)
