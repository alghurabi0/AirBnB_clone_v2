#!/usr/bin/python3
"""Database sql storage"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy.orm import sessionmaker
from models.place import Place
from models.review import Review
from sqlalchemy.orm import scoped_session
from models.amenity import Amenity
from models.user import User
from models.state import State


class DBStorage:
    """ database storage sql"""
    __engine = None
    __session = None

    def __init__(self):
        """ Initilization of instance"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ all method for queries """
        if cls is None:
            dicts = self.__session.query(State).all()
            dicts.extend(self.__session.query(City).all())
            dicts.extend(self.__session.query(Review).all())
            dicts.extend(self.__session.query(User).all())
            dicts.extend(self.__session.query(Amenity).all())
            dicts.extend(self.__session.query(Place).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            dicts = self.__session.query(cls)
        return {"{}.{}".format(type(x).__name__, x.id): x for x in dicts}

    def new(self, obj):
        """ add new obj to session"""
        self.__session.add(obj)

    def save(self):
        """commit self for now"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete of not none"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload and start new sess"""
        Base.metadata.create_all(self.__engine)
        sess = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(sess)
        self.__session = Session()

    def close(self):
        """close session"""
        self.__session.close()