import requests
from requests import post
import pytest

url = "https://reqres.in/api/unknown/23"

def test_step1():
    response = requests.get(url)
    response_body = response.json()
    print(response_body)
    assert response.status_code == 404