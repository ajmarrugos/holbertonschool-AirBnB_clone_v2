#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
        name = Column(String(128), nullable=False)
    else:
        name = ''
        state_id = '' 
