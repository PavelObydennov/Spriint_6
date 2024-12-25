import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..locators.order_page_locators import OrderPageLocators

class OrderPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Заполнение поля "Имя" значением: {first_name}')
    def fill_first_name(self, first_name):
        # Заполняет поле 'Имя'
        first_name_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.order_input_first_name))
        first_name_field.send_keys(first_name)

    @allure.step('Заполнение поля "Фамилия" значением: {last_name}')
    def fill_last_name(self, last_name):
        # Заполняет поле 'Фамилия'
        last_name_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.order_input_last_name))
        last_name_field.send_keys(last_name)

    @allure.step('Заполнение поля "Адрес" значением: {address}')
    def fill_address(self, address):
        # Заполняет поле 'Адрес'
        address_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.order_input_address))
        address_field.send_keys(address)

    @allure.step('Выбор первой станции метро из выпадающего списка')
    def select_metro_station_top_button(self):
        # Выбирает первую станцию метро из выпадающего списка
        metro_station_field_for_top_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.order_input_metro_station))
        metro_station_field_for_top_button.click()

        first_suggestion = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.metro_station_first_suggestion))
        first_suggestion.click()

    @allure.step('Выбор первой станции метро из выпадающего списка')
    def select_metro_station_bottom_button(self):
        # Выбирает первую станцию метро из выпадающего списка
        metro_station_field_for_bottom_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.order_input_metro_station))
        metro_station_field_for_bottom_button.click()

        second_suggestion = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.metro_station_second_suggestion))
        second_suggestion.click()

    @allure.step('Заполнение поля "Телефон" значением: {phone_number}')
    def fill_phone_number(self, phone_number):
        # Заполняет поле 'Телефон'
        phone_number_field = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(OrderPageLocators.order_input_number_phone))
        phone_number_field.send_keys(phone_number)

    @allure.step('Нажатие кнопки "Далее"')
    def click_next_button(self):
        # Нажимает кнопку 'Далее'
        next_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(OrderPageLocators.order_page_locators_button_next))
        next_button.click()