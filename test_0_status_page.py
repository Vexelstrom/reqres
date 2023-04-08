import requests
from requests import post
import pytest

#ТЕСТ №0 - ПРОВЕРКА УСПЕШНОГО ЗАПРОСА (КОД 200)
#Проверяем что страница проекта открывается и отправляется положительный запрос

def test_status_200():
    response = requests.get("https://reqres.in/")
    assert response.status_code == 200