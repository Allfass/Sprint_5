import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from random import randint
import random
import string

def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@pytest.fixture
def driver():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.get("https://stellarburgers.nomoreparties.site/")
    return driver

@pytest.fixture
def credentials():
    credentials = {}
    credentials['user'] = f'{randomword(8)}'
    credentials['mail'] = f'{randomword(8)}@ya.ru'
    credentials['password'] = f'{randint(1000000, 9999999)}'
    return credentials