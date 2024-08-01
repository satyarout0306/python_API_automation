import requests
from config.config import BASE_URL, HEADERS


def get(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url, headers=HEADERS)
    return response


def post(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=data, headers=HEADERS)
    return response


def put(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    response = requests.put(url, json=data, headers=HEADERS)
    return response


def patch(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    response = requests.patch(url, json=data, headers=HEADERS)
    return response


def delete(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.delete(url, headers=HEADERS)
    return response
