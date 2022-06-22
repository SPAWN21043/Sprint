from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    fam = Column(String)
    name = Column(String)
    otc = Column(String)

    pass_add = relationship("Pass", back_populates="users")


class Coord(Base):
    __tablename__ = "coords"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    height = Column(Integer)

    pass_add = relationship("Pass", back_populates="coord")


'''class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    pass_id = Column(Integer, ForeignKey('pass_added.id'))

    pass_add = relationship("Pass", back_populates="image")'''


class Pass(Base):
    __tablename__ = "pass_added"

    id = Column(Integer, primary_key=True, index=True)
    beautyTitle = Column(String)
    title = Column(String)
    other_titles = Column(String)
    connect = Column(String)
    add_time = datetime
    winter = Column(String)
    summer = Column(String)
    autumn = Column(String)
    spring = Column(String)
    user = Column(Integer, ForeignKey("users.id"))
    coords = Column(Integer, ForeignKey("coords.id"))

    users = relationship("User", back_populates="pass_add")
    coord = relationship("Coord", back_populates="pass_add")
    '''image = relationship("Image", back_populates="passs")'''
