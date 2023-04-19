#!/usr/bin/python3

"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.

Usage: ./file_name.py <mysql username> <mysql password> <database name> \
                       <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    state_name = sys.argv[4]

    c = db.cursor()
    c.execute("SELECT * FROM `states` WHERE `name` LIKE '{:s}' ORDER BY \
              id ASC".format(state_name))

    states = c.fetchall()
    for state in states:
        if state[1] == state_name:
            print(state)

    c.close()
    db.close()
