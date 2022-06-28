from fastapi.testclient import TestClient

from main import app
from sql_app import schemas

client = TestClient(app)


data_create = {
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
    "images": [{"image_url": "",
                "title": "Седловина"},
               {"image_url": "",
                "title": "Подъем"}]
}


data_get = {
  "status": 200,
  "message": "Объект получен",
  "id": {
    "id": 1,
    "title": "Пхия",
    "connect": "",
    "winter": "",
    "autumn": "1А",
    "status": "new",
    "coords": {
      "latitude": 45.3842,
      "height": 1200,
      "id": 1,
      "longitude": 7.1525
    },
    "beautyTitle": "пер. ",
    "other_titles": "Триев",
    "add_time": "2021-09-22T13:18:13",
    "summer": "1А",
    "spring": "",
    "user": {
      "email": "user@email.tld",
      "fam": "Пупкин",
      "otc": "Иванович",
      "phone": "79031234567",
      "id": 1,
      "name": "Василий"
    },
    "images": [
      {
        "image_url": "",
        "id_pass": 1,
        "title": "Седловина",
        "id": 1
      },
      {
        "image_url": "",
        "id_pass": 1,
        "title": "Подъем",
        "id": 2
      }
    ]
  }
}


def test_create_pass():
    response = client.post("/submitData/", json=data_create)
    assert response.status_code == 200
    assert response.json()


def test_get_id():
    response = client.get("/submitData/1")
    assert response.status_code == 200
    assert response.json() == data_get
