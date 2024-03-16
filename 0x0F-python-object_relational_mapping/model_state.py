#!/usr/bin/python3
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
mymetadata = MetaData()
base = declarative_base(metadata=mymetadata)

class State(base):
    """
    Class State with class attributes id and name
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False,primary_key=True)
    name = Column(String(128), nullable=False)
