# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Inventory(Base):
    __tablename__ = 'Inventory'

    id = Column(Integer, primary_key=True)
    produk_name = Column(String)
    quantity = Column(Integer)
    sale_price = Column(Integer)


class Person(Base):
    __tablename__ = 'Person'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)


class PersonDetail(Base):
    __tablename__ = 'PersonDetail'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    address = Column(String)


t_sqlite_sequence = Table(
    'sqlite_sequence', metadata,
    Column('name', NullType),
    Column('seq', NullType)
)


class AccessAuthor(Base):
    __tablename__ = 'AccessAuthor'

    id = Column(Integer, primary_key=True)
    name_authorization = Column(String, nullable=False)
    id_person = Column(ForeignKey('Person.id'), nullable=False)

    Person = relationship('Person')
