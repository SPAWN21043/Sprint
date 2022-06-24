from sqlalchemy.orm import Session
from . import models, schemas
import datetime


# Запрос по id
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# Запрос по email
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# Лимит на запросы
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# Запрос на создание пользователя
def create_user(db: Session, user: schemas.UserCreate):

    db_user = get_user_by_email(db, email=user.email)

    if db_user is None:
        db_users = models.User(**user.dict())
        db.add(db_users)
        db.commit()
        db.refresh(db_users)
        return db_users.id
    else:
        db_users = db_user
        return db_users.id


# Запрос на создание координат
def create_coord(db: Session, coords: schemas.CoordCreate):

    db_coord = models.Coord(**coords.dict())

    db.add(db_coord)
    db.commit()
    db.refresh(db_coord)

    return db_coord.id


# Запрос на поиск перевала и создание запроса на добавление картинок
def search_pass(db: Session, new_pereval: int, image: schemas.ImageCreate):

    for i in image:

        db_coord = models.Image(**i.dict())

        db_coord.id_pass = new_pereval

        db.add(db_coord)

    db.commit()


# Запрос на создание перевала
def create_pass(db: Session, item: schemas.PassCreate) -> object:

    db_pass = models.Pass(
        beautyTitle=item.beautyTitle,
        title=item.title,
        other_titles=item.other_titles,
        connect=item.connect,
        add_time=item.add_time,
        user=item.user,
        coords=item.coords,
        winter=item.winter,
        summer=item.summer,
        autumn=item.autumn,
        spring=item.spring,
    )

    db_pass.status = 'new'
    db_pass.date_added = datetime.datetime.now()

    db.add(db_pass)
    db.commit()
    db.refresh(db_pass)

    return db_pass.id
