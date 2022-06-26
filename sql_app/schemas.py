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


class PassBase(BaseModel):
    id: int
    beautyTitle: str
    title: str
    other_titles: str
    connect: str
    winter: str
    summer: str
    autumn: str
    spring: str
    user: Optional[UserCreate]
    coords: Optional[CoordCreate]
    images: Optional[List[ImageCreate]]


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


class PassAddedUpdate(BaseModel):  # Схема обновления
    beauty_title: Union[str, None] = None
    title: Union[str, None] = None
    other_titles: Union[str, None] = None
    connect: Union[str, None] = None
    winter: Union[str, None] = None
    summer: Union[str, None] = None
    autumn: Union[str, None] = None
    spring: Union[str, None] = None
    coords: Union[CoordCreate, None] = None
    '''images: Union[List[ImageCreate], None] = None'''

    class Config:
        schema_extra = {
            'example': {
                'beauty_title': 'пер.',
                'title': 'Гроза',
                'other_titles': 'Третьев',
                'connect': ', ',
                'winter': '1Б',
                'summer': '1А',
                'autumn': '1А',
                'spring': '1А',
                'coords': {
                    'latitude': 56.2368,
                    'longitude': 41.683,
                    'height': 120,
                },
                "images":
                    [{"image_url": "media/1",
                      "title": "Спуск"},
                     {"image_url": "media/2",
                      "title": "Вершина"}]
            }
        }


class Pass(PassCreate):
    id: int
    status: str
    user: int
    coord: int

    class Config:
        orm_mode = True
