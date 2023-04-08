import requests
from requests import post
import pytest

url = "https://reqres.in/api/login"



def test_step1():
    payload = {"email": "peter@klaven"}
    response = requests.request("POST", url, data=payload)
    response_body = response.json()
    assert (response_body["error"]) == "Missing password"
    assert response.status_code == 400