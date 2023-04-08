import requests
from requests import post
import pytest

url = "https://reqres.in/api/users/2"

def test_step1():
    response = requests.get(url)
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["data"]["id"] == 2
    assert response_body["data"]["first_name"] == "Janet"
    assert response_body["data"]["email"] == "janet.weaver@reqres.in"
