from selenium import webdriver
import pytest
import requests
from requests import post
import time

url = "https://reqres.in/"

@pytest.mark.usefixtures("chrome_driver")
class Test:
    def test_step1_web(self):
        self.driver.get(url)
        self.driver.find_element("xpath", "//*[@id='console']/div[1]/ul/li[1]").click()
        self.driver.find_element("xpath", "/html/body/div[2]/div/div/section[1]/div[2]/div[2]/pre[contains(text(), 'michael.lawson@reqres.in')]")
        time.sleep(5)

    def test_step2_api(self):
        response = requests.get("https://reqres.in/api/users?page=2")
        response_body = response.json()
        search_cortege = 0
        assert response_body["data"][search_cortege]["first_name"] == "Michael"
        assert response_body["data"][search_cortege]["email"] == "michael.lawson@reqres.in"