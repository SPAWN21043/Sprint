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


def test_create_pass():
    response = client.post("/submitData/", json=data_create)
    assert response.status_code == 200
    assert response.json()


def test_get_id():
    response = client.get("/submitData/1")
    assert response.status_code == 200
    assert response.json()


def test_get_email_all():
    response = client.get("/submitDate/user%40email.tld")
    assert response.status_code == 200
    assert response.json()


data_update = {
  "id": 2,
  "beauty_title": "пер.",
  "title": "Гроза",
  "other_titles": "Третьев",
  "connect": ", ",
  "winter": "1Б",
  "summer": "1А",
  "autumn": "1А",
  "spring": "1А",
  "coords": {
    "latitude": 56.2368,
    "longitude": 41.683,
    "height": 120
  },
  "images": [
    {
      "id": 3,
      "image_url": "media/1",
      "title": "Спуск",
      "id_pass": 1
    },
    {
      "id": 4,
      "image_url": "media/1",
      "title": "Равнина",
      "id_pass": 1
    }
  ]
}


def test_patch_id():
    response = client.patch("/submitData/2", json=data_update)
    assert response.status_code == 200
    assert response.json()

