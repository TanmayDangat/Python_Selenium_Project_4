from selenium import webdriver

import pytest


@pytest.fixture()
def setUp():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    return driver