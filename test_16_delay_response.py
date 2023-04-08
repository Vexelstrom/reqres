import requests
from requests import post
import pytest
import time

url = "https://reqres.in/api/users?delay=3"

def test_step1():
    response = requests.get(url)
    time.sleep(5)
    response_body = response.json()
    assert response_body["data"][0]["email"] == "george.bluth@reqres.in"
    assert response_body["data"][1]["email"] == "janet.weaver@reqres.in"
    assert response.status_code == 200