import requests
from requests import post
import pytest

url = "https://reqres.in/api/users/2"

def test_step1():
    response = requests.delete(url)
    assert response.status_code == 204