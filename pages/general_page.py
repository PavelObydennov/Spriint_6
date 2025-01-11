import allure
from pages.base_page import BasePage
from locators.general_page_locators import GeneralPageLocators
from locators.base_page_locators import BasePageLocators
from data.urls import url_dzen, base_url

class GeneralPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Заказать" сверху')
    def click_order_top_button(self):
        self.click_element(BasePageLocators.order_top_button)

    @allure.step('Нажатие кнопки "Заказать" внизу страницы')
    def click_order_bottom_button(self):
        self.click_element(GeneralPageLocators.order_bottom_button)

    @allure.step('Клик по логотипу Самоката')
    def click_logo_scooter(self):
        self.click_element(BasePageLocators.logo_scooter)

    @allure.step('Клик по логотипу Яндекса')
    def click_logo_yandex(self):
        self.click_element(BasePageLocators.logo_Yandex)

    @allure.step('Нажимаем нижнюю кнопку "Заказать" на главной странице')
    def click_order_bottom_and_wait_for_form(self):
        self.click_order_bottom_button()
        self.wait_for_element_visibility(BasePageLocators.check_locator_one)

    @allure.step('Проверяем вопрос и ответ')
    def verify_question_and_answer(self, question_method, answer_locator, expected_answer):
        self.scroll_to_bottom()
        getattr(self, question_method)()
        actual_answer = self.get_element_text(answer_locator)
        assert actual_answer == expected_answer

    @allure.step('Нажатие на вопрос')
    def click_question(self, question_locator):
        self.click_element(question_locator)

    @allure.step('Проверяем статус заказа')
    def check_order_status(self):
        self.wait_for_element_visibility(BasePageLocators.check_locator_two)
        order_status = self.get_element_text(BasePageLocators.check_locator_two)
        expected_status = 'Отменить заказ'
        assert order_status == expected_status
