import pytest
from selenium import webdriver

from constants import TestUrl


@pytest.fixture(scope='class')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get(TestUrl.BASE_URL)
    yield driver
    driver.quit()

