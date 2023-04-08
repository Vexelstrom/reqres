import requests
from requests import post
import pytest

url = "https://reqres.in/api/login"



def test_step1():
    payload = {"email": "eve.holt@reqres.in",
               "password": "cityslicka"}
    response = requests.request("POST", url, data=payload)
    response_body = response.json()
    assert len(response_body["token"]) != 0
    assert response.status_code == 200