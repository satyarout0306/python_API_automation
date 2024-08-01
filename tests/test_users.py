import pytest
from utils.helpers import get, post, put, patch, delete


# def test_create_user():
#     user_data = {
#         "name": "T Test",
#         "email": "ttest@example.com",
#         "gender": "male",
#         "status": "inactive"
#     }
#     response = post("/users", user_data)
#     assert response.status_code == 201
#     assert response.json()["name"] == "T Test"


def get_all_users():
    response = get("/users/")
    if response.status_code == 200:
        users = response.json()
        for user in users['gender'] == 'male':
            print(f'ID: {user['id']}, Name: {user['name']} ')

get_all_users()


# def test_get_user():
#     response = get("/users/6980123")
#     print("Response::", response)
#     name = response.json().get("name")
#     gender = response.json().get("gender")
#     print(f'Username is : {name} and gender is {gender}')
#     assert response.status_code == 200
#     assert response.json()["id"] == 6980123
#
#
# def test_update_user():
#     user_data = {
#         "name": "John Doe Updated"
#     }
#     response = put("/users/6980122", user_data)
#     print("Response:: ", response)
#     assert response.status_code == 200
#     updated_name = response.json().get("name")
#     print(updated_name)
#     assert response.json()["name"] == "John Doe Updated"

#
# def test_delete_user():
#     response = delete("/users/6940144")
#     assert response.status_code == 204
