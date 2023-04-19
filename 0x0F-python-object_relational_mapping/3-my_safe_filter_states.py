#!/usr/bin/python3

"""
Once again, write a script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument. But this
time, write one that is safe from MySQL injections!

Usage: ./file_name.py <mysql username> <mysql password> <database name> \
                       <state name searched>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
              (sys.argv[4],))

    states = c.fetchall()
    for state in states:
        print(state)

    c.close()
    db.close()
