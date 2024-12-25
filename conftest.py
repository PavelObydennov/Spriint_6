# # Здесь хранятся фикстуры
import  pytest
from selenium import webdriver

@pytest.fixture(params=['firefox', 'chrome'])
def setup(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    else:
        raise ValueError('Unknown browser type')
    driver.maximize_window()
    driver.get('https://qa-scooter.praktikum-services.ru/')
    yield driver
    driver.quit()
