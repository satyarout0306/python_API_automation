import pytest
from utils.helpers import get, post, put, delete


def test_get_users():
    response = get("/users")
    assert response.status_code == 200
    assert "users" in response.json()


def test_create_user():
    user_data = {
        "name": "John Doe",
        "email": "john.doe@example.com"
    }
    response = post("/users", user_data)
    assert response.status_code == 201
    assert response.json()["name"] == "John Doe"


def test_update_user():
    user_data = {
        "name": "John Doe Updated"
    }
    response = put("/users/1", user_data)
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe Updated"


def test_delete_user():
    response = delete("/users/1")
    assert response.status_code == 204
