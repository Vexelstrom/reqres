import requests
from requests import post
import pytest

url = "https://reqres.in/api/register"



def test_step1():
    payload = {"email": "eve.holt@reqres.in",
               "password": "pistol"}
    response = requests.request("POST", url, data=payload)
    response_body = response.json()
    assert (response_body["id"]) != 0
    assert len(response_body["token"]) != 0
    assert response.status_code == 200