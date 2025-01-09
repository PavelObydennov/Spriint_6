import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.general_page_locators import GeneralPageLocators
from locators.base_page_locators import BasePageLocators
from data.urls import url_dzen, base_url

class GeneralPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Нажатие кнопки "Заказать" внизу страницы')
    def click_order_bottom_button(self):
        self.wait_and_click(GeneralPageLocators.order_bottom_button)

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

    @allure.step('Нажатие на первый вопрос')
    def click_question_one(self):  # 1
        self.wait_and_click(GeneralPageLocators.question_one)

    @allure.step('Нажатие на второй вопрос')
    def click_question_two(self):  # 2
        self.wait_and_click(GeneralPageLocators.question_two)

    @allure.step('Нажатие на третий вопрос')
    def click_question_three(self):  # 3
        self.wait_and_click(GeneralPageLocators.question_three)

    @allure.step('Нажатие на четвертый вопрос')
    def click_question_four(self):  # 4
        self.wait_and_click(GeneralPageLocators.question_four)

    @allure.step('Нажатие на пятый вопрос')
    def click_question_five(self):  # 5
        self.wait_and_click(GeneralPageLocators.question_five)

    @allure.step('Нажатие на шестой вопрос')
    def click_question_six(self):  # 6
        self.wait_and_click(GeneralPageLocators.question_six)

    @allure.step('Нажатие на седьмой вопрос')
    def click_question_seven(self):  # 7
        self.wait_and_click(GeneralPageLocators.question_seven)

    @allure.step('Нажатие на восьмой вопрос')
    def click_question_eight(self):  # 8
        self.wait_and_click(GeneralPageLocators.question_eight)