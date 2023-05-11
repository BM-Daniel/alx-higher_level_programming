#!/usr/bin/python3

"""
Write a script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa

Usage: ./file_name.py <mysql username> <mysql password> <database name>
"""

from sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    for s in session.query(State):
        if "a" in s.name:
            session.delete(s)

    session.commit()
