import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.base_page_locators import BasePageLocators
from locators.rent_page_locators import RentPageLocators

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

    def wait_for_url(self, expected_url, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание видимости элемента")
    def wait_for_element_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_rent_page_load(self, timeout=10):
        self.wait_for_element_visibility(RentPageLocators.rent_page_next_button, timeout)

    @allure.step("Прокрутка страницы до середины")
    def scroll_to_middle(self):
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        self.driver.execute_script(f"window.scrollTo(0, {total_height * 2 // 3});")