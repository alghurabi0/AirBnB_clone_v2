#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String
from models.city import City
from models.base_model import BaseModel
import models
from models.base_model import Base
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            cl = []
            for c in list(models.storage.all(City).values()):
                if c.state_id == self.id:
                    cl.append(c)
            return cl
