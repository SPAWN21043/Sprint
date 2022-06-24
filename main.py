from http.client import HTTPException
from typing import List

from fastapi import FastAPI, Depends
from fastapi.encoders import jsonable_encoder

from sql_app import schemas, crud
from sql_app.database import SessionLocal
from sql_app.errors import ErrorConnectionServer, get_json_response, ErrorCreatingRecord
from sqlalchemy.orm import Session

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/submitData/', response_model=schemas.PassCreate)
def post_pass(item: schemas.PassCreate, db: Session = Depends(get_db)):  # Название изменено так как не должно быть больших букв в названии

    try:  # Проверка на подключение к базе
        db.execute('SELECT * FROM users')
    except Exception as error:
        raise ErrorConnectionServer(f'Ошибка соединения: {error}')

    news_user = crud.create_user(db=db, user=item.user)  # Создание пользователя
    new_coord = crud.create_coord(db=db, coords=item.coords)  # Создание координат

    item.user = news_user
    item.coords = new_coord

    new_pereval = crud.create_pass(db=db, item=item)  # Создание перевала

    crud.search_pass(db=db, new_pereval=new_pereval, image=item.images)  # Создание информации о картинках

    return get_json_response(200, "Отправлено", new_pereval)


@app.get('/submitData/{id}', response_model=schemas.PassCreate)
def search_pass(id: int, db: Session = Depends(get_db)):
    item = crud.get_pass(db=db, id=id)  # Запрос о перевале по id
    return get_json_response(200, 'Объект получен', jsonable_encoder(item))
