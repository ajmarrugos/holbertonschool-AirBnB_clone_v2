#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            """ Getter method """
                pass

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
