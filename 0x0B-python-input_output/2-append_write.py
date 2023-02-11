#!/usr/bin/python3

"""
Write a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Append to file function

    Args:
        filename (str): Name of file to be appended to
        text (str): Text to be appeended to file

    Returns:
        Number of characters appended to file
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
