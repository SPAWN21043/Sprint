from typing import List, Union, Optional
from pydantic import BaseModel, Field
from datetime import datetime


# Схемы моделей pydantic
class CoordCreate(BaseModel):
    latitude: float
    longitude: float
    height: int

    class Config:
        schema_extra = {
            'example': {
                "latitude": "45.3842",
                "longitude": "7.1525",
                "height": "1200",
            }
        }


class Coord(CoordCreate):
    id: int
    pass_id: int
    pass_add: 'Pass'

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    email: str
    phone: str
    fam: str
    name: str
    otc: str

    class Config:
        schema_extra = {
            'example': {
                "email": "user@email.tld",
                "phone": "79031234567",
                "fam": "Пупкин",
                "name": "Василий",
                "otc": "Иванович",
            }
        }


class User(UserBase):
    id: int
    pass_id: int
    pass_add: 'Pass'

    class Config:
        orm_mode = True


class ImageCreate(BaseModel):
    image_url: str
    title: str


class Image(ImageCreate):
    id: int
    images: List[ImageCreate]

    class Config:
        orm_mode = True


class PassCreate(BaseModel):
    beautyTitle: str
    title: str
    other_titles: str
    connect: str
    add_time: datetime
    winter: str
    summer: str
    autumn: str
    spring: str
    user: Optional[UserCreate]
    coords: Optional[CoordCreate]
    images: Optional[List[ImageCreate]]

    class Config:
        schema_extra = {
            'example': {
                "beautyTitle": "пер. ",
                "title": "Пхия",
                "other_titles": "Триев",
                "connect": "",
                "add_time": "2021-09-22 13:18:13",
                "winter": "",
                "summer": "1А",
                "autumn": "1А",
                "spring": "",
                "user": {
                    "email": "user@email.tld",
                    "phone": "79031234567",
                    "fam": "Пупкин",
                    "name": "Василий",
                    "otc": "Иванович"
                },
                "coords": {
                    "latitude": "45.3842",
                    "longitude": "7.1525",
                    "height": "1200",
                },
                "images":
                    [{"image_url": "",
                      "title": "Седловина"},
                     {"image_url": "",
                      "title": "Подъем"}]
            }
        }


class Pass(PassCreate):
    id: int
    status: str
    user: int
    coord: int

    class Config:
        orm_mode = True
