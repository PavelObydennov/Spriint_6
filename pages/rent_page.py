import allure
from selenium.webdriver.common.by import By
from ..locators.rent_page_locators import RentPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RentPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Выбор даты доставки самоката на 25 декабря 2024')
    def fill_date_delivery_of_scooter_for_top_button(self):
        date_field_for_top_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.date_delivery_of_scooter))
        date_field_for_top_button.click()

        date_field_for_top_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.choose_first_date_delivery_of_scooter))
        date_field_for_top_button.click()

    @allure.step('Выбор даты доставки самоката на 1 января 2025')
    def fill_date_delivery_of_scooter_for_bottom_button(self):
        date_field_for_bottom_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.date_delivery_of_scooter))
        date_field_for_bottom_button.click()

        date_field_for_bottom_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.choose_first_date_delivery_of_scooter))
        date_field_for_bottom_button.click()

    @allure.step('Выбор срока аренды на сутки')
    def click_period_rental_for_top_button(self):
        # Кликаем по полю срока аренды
        period_field_for_top_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.period_rental))
        period_field_for_top_button.click()

        # Выбираем первый элемент из списка
        first_option_day_one = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.day_one_period_rental))
        first_option_day_one.click()

    @allure.step('Выбор срока аренды на 3ое суток')
    def click_period_rental_for_bottom_button(self):
        # Кликаем по полю срока аренды
        period_field_for_bottom_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.period_rental))
        period_field_for_bottom_button.click()

        # Выбираем первый элемент из списка
        first_option_day_three = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.day_three_period_rental))
        first_option_day_three.click()

    @allure.step('Нажатие на кнопку "Заказать"')
    def click_button_order(self):
        order_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.button_order))
        order_button.click()

    @allure.step('Подтверждение заказа: Нажатие на кнопку "Да"')
    def click_button_order_confirmation(self):
        confirm_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.button_order_confirmation))
        confirm_button.click()

    @allure.step('Просмотр статуса заказа: Нажатие на кнопку "Статус"')
    def click_button_status(self):
        look_status = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(RentPageLocators.button_status))
        look_status.click()