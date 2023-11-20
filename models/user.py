#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """Represents a user for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table users.

    Attributes:
        __tablename__ (str): table name attr for sql.
        email: (sqlalchemy String): database attr.
        password (sqlalchemy String): password col.
        first_name (sqlalchemy String): firt name of the user.
        last_name (sqlalchemy String): last name of the use.
        places (sqlalchemy relationship): relationship between user and place.
        reviews (sqlalchemy relationship): relationship between user and rev.
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    places = relationship("Place", backref="user", cascade="delete")
    reviews = relationship("Review", backref="user", cascade="delete")