from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from . import models, schemas
import datetime


# Запрос по id
def get_user(db: Session, user_id: int):
    print(user_id)
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


def get_pass(db: Session, id: int) -> dict:

        c_pass = db.query(models.Pass).filter(models.Pass.id == id).first()
        user = db.query(models.User).filter(models.User.id == c_pass.user).first()
        coords = db.query(models.Coord).filter(models.Coord.id == c_pass.coords).first()
        image = db.query(models.Image).filter(models.Image.id_pass == id).first()

        json_user = jsonable_encoder(user)
        json_coords = jsonable_encoder(coords)
        json_images = jsonable_encoder(image)
        dict_pass = jsonable_encoder(c_pass)

        dict_pass['user'] = json_user
        dict_pass['coords'] = json_coords
        dict_pass['images'] = json_images

        return dict_pass


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


def update_pass(pass_id: int, db: Session, item: schemas.PassAddedUpdate) -> object:
    db_pass = db.query(models.Pass).filter(models.Pass.id == pass_id).first()

    db_pass.beauty_title = item.beauty_title
    db_pass.title = item.title
    db_pass.other_titles = item.other_titles
    db_pass.connect = item.connect
    db_pass.winter = item.winter
    db_pass.summer = item.summer
    db_pass.autumn = item.autumn
    db_pass.spring = item.spring

    if not db_pass.coords is None:
        db_coords = db.query(models.Coord).filter(models.Coord.id == db_pass.coords).first()

        db_coords.latitude = item.coords.latitude
        db_coords.longitude = item.coords.longitude
        db_coords.height = item.coords.height

        db.add(db_coords)
        db.commit()
        db.refresh(db_coords)
    else:
        db_coords = create_coord(db, item.coords)
        db_pass.coords_id = db_coords.id

    db.add(db_pass)
    db.commit()
    db.refresh(db_pass)

    return db_pass.id
