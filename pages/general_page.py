import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.general_page_locators import GeneralPageLocators

class GeneralPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Нажатие кнопки "Заказать" внизу страницы')
    def click_order_bottom_button(self):
        # Нажимает кнопку "Заказать", которая находится внизу страницы.
        button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(GeneralPageLocators.order_bottom_button))
        button.click()

    @allure.step('Нажатие на вопрос: {question_locator}')
    def click_question(self, question_locator):
        # Нажимает на вопрос из выпадающего списка, указанный локатором.
        question = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(question_locator))
        question.click()

    @allure.step('Нажатие на первый вопрос')
    def click_question_one(self): # 1
        self.driver.find_element(*GeneralPageLocators.question_one).click()

    @allure.step('Нажатие на второй вопрос')
    def click_question_two(self): # 2
        self.driver.find_element(*GeneralPageLocators.question_two).click()

    @allure.step('Нажатие на третий вопрос')
    def click_question_three(self): # 3
        self.driver.find_element(*GeneralPageLocators.question_three).click()

    @allure.step('Нажатие на четвертый вопрос')
    def click_question_four(self): # 4
        self.driver.find_element(*GeneralPageLocators.question_four).click()

    @allure.step('Нажатие на пятый вопрос')
    def click_question_five(self): # 5
        self.driver.find_element(*GeneralPageLocators.question_five).click()

    @allure.step('Нажатие на шестой вопрос')
    def click_question_six(self): # 6
        self.driver.find_element(*GeneralPageLocators.question_six).click()

    @allure.step('Нажатие на седьмой вопрос')
    def click_question_seven(self): # 7
        self.driver.find_element(*GeneralPageLocators.question_seven).click()

    @allure.step('Нажатие на восьмой вопрос')
    def click_question_eight(self): # 8
        self.driver.find_element(*GeneralPageLocators.question_eight).click()