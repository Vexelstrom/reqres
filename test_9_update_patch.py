import requests
from requests import post
import pytest

url = "https://reqres.in/api/users/2"

def test_step1():
    response = requests.patch(url, data={'name': 'morpheus', 'job': 'zion resident'})
    response_body = response.json()
    assert len(response_body["updatedAt"]) != 0
    assert response.status_code == 200