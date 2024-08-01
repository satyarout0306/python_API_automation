import pytest
from utils.helpers import get, post, put, patch, delete
from utils.access_excel import get_user_data_from_excel
from config.config import file_path


def test_create_user():
    user_data = {
        "name": "C Test",
        "email": "ctest@example.com",
        "gender": "female",
        "status": "active"
    }

    response = post("/users", user_data)
    assert response.status_code == 201
   # assert response.json()["name"] == "S Test"


def test_get_all_users():
    response = get("/users/")
    if response.status_code == 200:
        users = response.json()
        female_users = [user for user in users if user['gender'] == 'female']

        for user in female_users:
            print(f'ID: {user['id']}, Name: {user['name']} ')

print(test_get_all_users())


def test_get_user():
    response = get("/users/7150262")
    print("Response::", response)
    name = response.json().get("name")
    gender = response.json().get("gender")
    print(f'Username is : {name} and gender is {gender}')
    assert response.status_code == 200
    assert response.json()["id"] == 7150262


def test_update_user():
    user_data = {
        "name": "John Doe Updated"
    }
    response = put("/users/7150262", user_data)
    print("Response:: ", response)
    assert response.status_code == 200
    updated_name = response.json().get("name")
    print(updated_name)
    assert response.json()["name"] == "John Doe Updated"


def test_delete_user():
    response = delete("/users/6940144")
    assert response.status_code == 204
