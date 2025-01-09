import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.general_page_locators import GeneralPageLocators
from locators.base_page_locators import BasePageLocators
from locators.rent_page_locators import RentPageLocators
from data.urls import url_dzen, base_url

class GeneralPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Прокрутка страницы на заданную высоту")
    def scroll_to(self, y_position):
        self.driver.execute_script(f"window.scrollTo(0, {y_position});")

    @allure.step('Клик по кнопке "Заказать" сверху')
    def click_order_top_button(self):
        self.wait_for(EC.element_to_be_clickable(BasePageLocators.order_top_button)).click()

    @allure.step('Нажатие кнопки "Заказать" внизу страницы')
    def click_order_bottom_button(self):
        self.wait_and_click(GeneralPageLocators.order_bottom_button)

    @allure.step('Клик по логотипу Самоката')
    def click_logo_scooter(self):
        self.wait_for(EC.element_to_be_clickable(BasePageLocators.logo_scooter)).click()

    @allure.step('Клик по логотипу Яндекса')
    def click_logo_yandex(self):
        self.wait_for(EC.element_to_be_clickable(BasePageLocators.logo_Yandex)).click()

    @allure.step("Ожидание загрузки страницы аренды")
    def wait_for_rent_page_load(self, timeout=10):
        self.wait_for_element_visibility(RentPageLocators.rent_page_next_button, timeout)

    @allure.step('Нажимаем нижнюю кнопку "Заказать" на главной странице')
    def click_order_bottom_and_wait_for_form(self):
        self.click_order_bottom_button()
        self.wait_for_element_visibility(BasePageLocators.check_locator_one)

    @allure.step('Проверяем вопрос и ответ')
    def verify_question_and_answer(self, question_method, answer_locator, expected_answer):
        # Прокрутка страницы до низа
        self.scroll_to_bottom()
        getattr(self, question_method)()

        actually_answer = self.wait_for_element_visibility(answer_locator).text.strip()

        # Проверка текста ответа
        assert actually_answer == expected_answer

    @allure.step('Нажатие на вопрос')
    def click_question(self, question_locator):
        self.wait_and_click(question_locator)

    @allure.step('Проверяем статус заказа')
    def check_order_status(self):
        self.wait_for_element_visibility(BasePageLocators.check_locator_two)

        order_status = self.wait_for_element_visibility(BasePageLocators.check_locator_two).text.strip()
        expected_status = 'Отменить заказ'

        assert order_status == expected_status

    @allure.step("Прокрутка страницы до середины")
    def scroll_to_middle(self):
        total_height = self.driver.execute_script("return document.body.scrollHeight")
        self.scroll_to(total_height * 2 // 3)

    @allure.step("Прокрутка страницы до низа")
    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def wait_and_click(self, locator, timeout=10):
        self.wait_for(EC.element_to_be_clickable(locator), timeout).click()

    def get_element_text(self, locator):
        element = self.wait_for_element_visibility(locator)
        return element.text
