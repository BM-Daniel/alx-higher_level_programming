#!/usr/bin/python3

"""
Write a Python file similar to model_state.py named model_city.py that contains
the class definition of a City.
You must use the module SQLAlchemy
"""

from model_state import Base
from sqlalchemy import Integer, String, Column, ForeignKey

class City(Base):
    """
    Class to represent a sql table called cities

    Attributes:
        __tablename__ (str): Name of the sql table
        id (sqlalchemy.Integer): The id of the state
        name (sqlalchemy.String): The name of the state
        state_id (sqlalchemy.Integer): Foreign key to states table
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
