import requests
from requests import post
import pytest

url = "https://reqres.in/api/unknown"

def test_step1():
    response = requests.get(url)
    response_body = response.json()
    assert response_body["data"][0]["name"] == "cerulean"
    assert response_body["data"][1]["name"] == "fuchsia rose"
    assert response.status_code == 200
