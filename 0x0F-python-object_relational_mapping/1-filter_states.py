#!/usr/bin/python3

"""
Write a script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa

Usage: ./file_name.py <mysql username> <mysql password> <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT * from `states` ORDER BY `id`")

    [print(state) for state in c.fetchall() if state[1][0] == "N"]
