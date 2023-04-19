#!/usr/bin/python3

"""
Write a python file that contains the class definition of a State and an
instance Base = declarative_base()
You must use the module SQLAlchemy
"""

from sqlalchemy import Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class to represent a sql table called states

    Attributes:
        __tablename__ (str): Name of the sql table
        id (sqlalchemy.Integer): The id of the state
        name (sqlalchemy.String): The name of the state
    """

    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
