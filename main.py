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
async def post_pass(item: schemas.PassCreate, db: Session = Depends(get_db)):  # Название изменено так как не должно быть больших букв в названии

    """
    Вызов функции создания записи о перевале, пользователе, координат и информации о фотографиях.
    :param item:
    :param db:
    :return:
    """

    try:  # Проверка на подключение к базе
        db.execute('SELECT * FROM users')
    except Exception as error:
        raise ErrorConnectionServer(f'Ошибка соединения: {error}')

    news_user = crud.create_user(db=db, user=item.user)  # Создание пользователя
    new_coord = crud.create_coord(db=db, coords=item.coords)  # Создание координат

    item.user = news_user
    item.coords = new_coord

    new_pass = crud.create_pass(db=db, item=item)  # Создание перевала

    crud.search_pass(db=db, new_pass=new_pass, image=item.images)  # Создание информации о картинках

    return get_json_response(200, "Отправлено", new_pass)


@app.get('/submitData/{id}', response_model=schemas.PassCreate)
def search_pass(id: int, db: Session = Depends(get_db)):
    item = crud.get_pass(db=db, id=id)  # Запрос о перевале по id
    return get_json_response(200, 'Объект получен', jsonable_encoder(item))


@app.patch("/submitData/{id}", response_model=schemas.PassCreate, response_model_exclude_none=True)
async def patch_submit_data_id(id: int, item: schemas.PassAddedUpdate, db: Session = Depends(get_db)):

    """
    Вызов функции получения информации о перевале.
    :param id: Параметр id записи перевала
    :param item: класс схемы
    :param db: сессия подключения
    :return: сообщение в JSON
    """

    # pending — если модератор взял в работу;
    # accepted — модерация прошла успешно;
    # rejected — модерация прошла, информация не принята.
    statuses = [
        'pending',
        'accepted',
        'rejected',
    ]

    db_pass_info = crud.get_pass(db, id)

    if db_pass_info is None:
        return get_json_response(422, f'Перевал с id {id} отсутствует')

    if db_pass_info['status'] in statuses:
        return get_json_response(422, f'Перевал с id {id} на модерации')

    update_pass = crud.update_pass(id, db, item)
    return get_json_response(200, 'Запись обновлена', update_pass)


@app.get('/submitDate/{email}', response_model=List[schemas.PassBase])
async def read_pass(email: str, db: Session = Depends(get_db)):

    """
    Запрос о перевалах созданных пользователем с фильтром по email.
    :param email: email пользователя
    :param skip: пропуск по id
    :param limit: лимит выборки по количеству записей
    :param db: сессия подключения
    :return: сообщение в JSON
    """
    pass_all = crud.search_all(db=db, email=email)
    return pass_all
