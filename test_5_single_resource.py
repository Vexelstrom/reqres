import requests
from requests import post
import pytest

url = "https://reqres.in/api/unknown/2"

def test_step1():
    response = requests.get(url)
    response_body = response.json()
    assert response_body["data"]["name"] == "fuchsia rose"
    assert response.status_code == 200