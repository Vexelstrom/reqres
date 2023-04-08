import pytest
from selenium import  webdriver
import requests

#версионные переменные
webdriver110 = webdriver.Chrome('c:\\chromedriver\\chromedriver.exe')


@pytest.fixture(scope="class")
def chrome_driver(request):
    driver = webdriver110 #Используемая версия вебдрайвера
    request.cls.driver = driver
    yield
    driver.close()