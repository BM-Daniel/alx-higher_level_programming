#!/usr/bin/python3

"""
prints all City objects from the database hbtn_0e_14_usa

Usage: ./file_name.py <mysql username> <mysql password> <database name>
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    data = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id)

    for city, state in data:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
