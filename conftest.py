# # Здесь хранятся фикстуры
import pytest
from selenium import webdriver
from data.urls import base_url

@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise ValueError('Unknown browser type')
    # driver.maximize_window()
    driver.get(base_url)
    yield driver
    driver.quit()
