import requests
from requests import post
import pytest

#ТЕСТ №1 - ПРОВЕРКА ЛИСТИНГА СТРАНИЦЫ СО СПИСКОМ ПОЛЬЗОВАТЕЛЕЙ
#Проверяем что мы находимся на страницк №2, и что в кортеже 0 записан искомый пользователь с искомомй почтой.

url = "https://reqres.in/api/users?page=2"

def test_step1():
    response = requests.get(url)
    response_body = response.json()
    assert response.status_code == 200
    assert response_body["page"] == 2

def test_step2():
    response = requests.get(url)
    response_body = response.json()
    search_cortege = 0
    assert response_body["data"][search_cortege]["first_name"] == "Michael"
    assert response_body["data"][search_cortege]["email"] == "michael.lawson@reqres.in"
