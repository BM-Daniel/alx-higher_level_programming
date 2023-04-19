#!/usr/bin/python3

"""
Write a script that lists all cities from the database hbtn_0e_4_usa

Usage: ./file_name.py <mysql username> <mysql password> <database name>
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
                   FROM `cities` as `c` \
                   INNER JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                   ORDER BY `c`.`id`")

    [print(city) for city in cursor.fetchall()]

    cursor.close()
    db.close()
