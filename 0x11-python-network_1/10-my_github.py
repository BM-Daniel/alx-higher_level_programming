#!/usr/bin/python3

"""
Write a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authenticate = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=authenticate)
    print(req.json().get("id"))
