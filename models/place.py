#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String, Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
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