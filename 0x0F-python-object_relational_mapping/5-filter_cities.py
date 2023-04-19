#!/usr/bin/python3

"""
Write a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa

Usage: ./file_name.py <mysql username> <mysql password> <database name> \
                      <state name>
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM `cities` as `c` \
                   INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                   ORDER BY `c`.`id`")

    print(", ".join([city[2] for city in cursor.fetchall()
                     if city[4] == argv[4]]))

    cursor.close()
    db.close()
