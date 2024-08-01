import pytest
from utils.helpers import get, post


def test_get_post_comments():
    response = get("/posts/6940144/comments")
    assert response.status_code == 200


def test_create_post_comment():
    comment_data = {
        "name": "Jane Doe",
        "email": "jane.doe@example.com",
        "body": "This is a comment."
    }
    response = post("/posts/6940144/comments", comment_data)
    assert response.status_code == 201
    assert response.json()["name"] == "Jane Doe"
