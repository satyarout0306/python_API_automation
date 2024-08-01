import pytest
from utils.helpers import get, post

def test_get_user_todos():
    response = get("/users/6940144/todos")
    assert response.status_code == 200


def test_create_user_todo():
    todo_data = {
        "title": "New Todo",
        "due_on": "2023-12-31T23:59:59.000+05:30",
        "status": "pending"
    }
    response = post("/users/6940144/todos", todo_data)
    assert response.status_code == 201
    assert response.json()["title"] == "New Todo"
