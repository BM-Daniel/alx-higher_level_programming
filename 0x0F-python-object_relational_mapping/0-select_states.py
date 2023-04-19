#!/usr/bin/python3

"""
Write a script that lists all states from the database hbtn_0e_0_usa
"""

from MySQLdb import _mysql
import sys

if __name__ == "__main__":
    db = _mysql.connect(user=sys.argv[1], password=sys.argv[2],
                        database=sys.argv[3])

    db.query(
        """
        SELECT * FROM `states`
        """
    )

    [print(state) for state in db.use_result()]
