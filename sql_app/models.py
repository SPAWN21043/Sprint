from datetime import datetime

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):  # Модель таблицы пользователя

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)
    fam = Column(String)
    name = Column(String)
    otc = Column(String)

    # Организация связи таблиц
    pass_add = relationship("Pass", back_populates="users")


class Coord(Base):  # Модель таблицы с координатами

    __tablename__ = "coords"

    id = Column(Integer, primary_key=True, index=True)
    latitude = Column(Float)
    longitude = Column(Float)
    height = Column(Integer)

    # Организация связи таблиц
    pass_add = relationship("Pass", back_populates="coord")


class Image(Base):  # Модель таблицы с информацией о картинках

    __tablename__ = 'images'

    id = Column(Integer, primary_key=True, index=True)
    image_url = Column(String)
    title = Column(String)
    id_pass = Column(Integer, ForeignKey("pass_added.id"))

    # Организация связи таблиц
    owner = relationship("Pass", back_populates="images")


class Pass(Base):  # Модель таблицы перевалов

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
    status = Column(String)
    user = Column(Integer, ForeignKey("users.id"))
    coords = Column(Integer, ForeignKey("coords.id"))

    # Организация связи таблиц
    users = relationship("User", back_populates="pass_add")
    coord = relationship("Coord", back_populates="pass_add")
    images = relationship("Image", back_populates="owner")

