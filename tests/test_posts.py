import pytest
from utils.helpers import get, post


def test_get_user_posts():
    response = get("/users/6940144/posts")
    assert response.status_code == 200


def test_create_user_post():
    post_data = {
        "title": "New Post",
        "body": "This is the body of the new post."
    }
    response = post("/users/6940144/posts", post_data)
    assert response.status_code == 201
    assert response.json()["title"] == "New Post"
