#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.review import Review
from models.amenity import Amenity


at = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"),
                                 primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"),
                                 primary_key=True, nullable=False))



class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    city_id = Column(String(128), ForeignKey("cities.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_bathrooms = Column(Integer, default=0)
    latitude = Column(Float)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    number_rooms = Column(Integer, default=0)
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE", None) != "db":
        @property
        def reviews(self):
            """reviews relationship for fileStorage"""
            rvs = []
            for rv in list(models.storage.all(Review).values()):
                if rv.place_id == self.id:
                    rvs.append(rv)
            return rvs

        @property
        def amenities(self):
            """amenities relationshio for fileStorage"""
            ams = []
            for am in list(models.storage.all(Amenity).values()):
                if am.id in self.amenity_ids:
                    ams.append(am)
            return ams

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)