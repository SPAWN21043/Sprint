from fastapi import FastAPI, File, UploadFile, Depends
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
def post_pass(item: schemas.PassCreate, db: Session = Depends(get_db)):
    print(item)

    try:
        db.execute('SELECT * FROM users')
    except Exception as error:
        raise ErrorConnectionServer(f'Ошибка соединения: {error}')

    news_user = crud.create_user(db=db, user=item.user)

    new_coords = crud.create_coord(db=db, coords=item.coord)

    item.user = news_user
    item.coord = new_coords

    new_pereval = crud.create_pass(db=db, item=item)

    return get_json_response(200, 'Отправлено', new_pereval.id)
