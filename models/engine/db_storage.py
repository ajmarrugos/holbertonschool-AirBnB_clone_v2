#!/usr/bin/python3
""" New Engine as DBStorage """
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.schema import MetaData

engine =create_engine('')

class DBStorage:
    """"DBStorage """
    __engine = None
    __session = None
