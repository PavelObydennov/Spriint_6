import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.base_page_locators import BasePageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver


    @allure.step('Клик по кнопке "Заказать" сверху')
    def click_order_top_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.order_top_button)).click()

    @allure.step('Клик по логотипу Самоката')
    def click_logo_scooter(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.logo_scooter)).click()

    @allure.step('Клик по логотипу Яндекса')
    def click_logo_yandex(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(BasePageLocators.logo_Yandex)).click()
