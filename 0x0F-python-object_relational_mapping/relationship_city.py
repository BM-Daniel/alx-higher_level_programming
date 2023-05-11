#!/usr/bin/python3

"""
Improve the files model_city.py and model_state.py, and save them as
relationship_city.py and relationship_state.py
"""

from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Blueprint for a city class

    Attributes:
        id (sqlalchemy.Column): id of the city
        name (sqlalchemy.Column): name of the city
        state_id (sqlalchemy.Column): state id of the city
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
