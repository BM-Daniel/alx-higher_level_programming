#!/usr/bin/python3

"""
Write a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import urllib.request as url_req
import urllib.error as url_err
import sys


if __name__ == "__main__":
    try:
        with url_req.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))

    except url_err.HTTPError as error:
        print('Error code:', error.code)
