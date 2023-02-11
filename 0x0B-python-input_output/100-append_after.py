#!/usr/bin/python3

"""
Write a function that inserts a line of text to a file, after each line
containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Function to be used for update

    Args:
        filename (str): Name of the file
        search_string (str): String to look for in the file
        new_string (Str): The string to fix in
    """

    text = ""

    with open(filename) as f:
        for line in f:
            text += line

            if search_string in line:
                text += new_string

    with open(filename, "w") as f:
        f.write(text)
