import requests
from requests import post
import pytest

url = "https://reqres.in/api/users"



def test_step1():
    payload = {"name": "morpheus",
               "job": "leader"}
    response = requests.request("POST", url, data=payload)
    response_body = response.json()
    assert response_body["id"]
    assert len(response_body["createdAt"]) != 0
    assert response.status_code == 201