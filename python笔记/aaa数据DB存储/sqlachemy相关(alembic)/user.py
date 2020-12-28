# coding: utf-8
from sqlalchemy import Column, Integer, Text, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(50), nullable=False, index=True)
    age = Column(Integer, nullable=False, index=True)


class Config(Base):
    __tablename__ = 'config'
    id = Column(Integer, primary_key=True, autoincrement=True)
    key = Column(String(50), index=True, nullable=False, unique=True)
    value = Column(String(256))
