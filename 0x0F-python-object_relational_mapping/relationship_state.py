#!/usr/bin/python3

"""
Improve the files model_city.py and model_state.py, and save them as
relationship_city.py and relationship_state.py
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """
    Blueprint for state class

    Attributes:
        __tablename__ (str): MySQL table name
        id (sqlalchemy.Integer): id of the state
        name (sqlalchemy.String): name of the state
        cities (sqlalchemy.orm.relationship): Relationship between State and
        City
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
