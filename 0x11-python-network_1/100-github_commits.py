#!/usr/bin/python3

"""
A script to list the 10 most recent commits of a repo
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    req = requests.get(url)
    repo_commits = req.json()

    try:
        for i in range(10):
            print("{}: {}".format(repo_commits[i].get("sha"),
                                  repo_commits[i].get("commit")
                                  .get("author").get("name")))

    except IndexError:
        pass
