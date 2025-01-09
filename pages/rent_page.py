import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from locators.rent_page_locators import RentPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from data.urls import url_dzen, base_url

class RentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Выбор даты доставки самоката на 16 января 2025')
    def fill_date_delivery_of_scooter_for_top_button(self):
        self.wait_and_select_date(RentPageLocators.date_delivery_of_scooter, RentPageLocators.choose_first_date_delivery_of_scooter)

    @allure.step('Выбор даты доставки самоката на 17 января 2025')
    def fill_date_delivery_of_scooter_for_bottom_button(self):
        self.wait_and_select_date(RentPageLocators.date_delivery_of_scooter, RentPageLocators.choose_second_date_delivery_of_scooter)

    @allure.step('Выбор срока аренды на сутки')
    def click_period_rental_for_top_button(self):
        self.wait_and_select_from_list(RentPageLocators.period_rental, RentPageLocators.day_one_period_rental)

    @allure.step('Выбор срока аренды на трое суток')
    def click_period_rental_for_bottom_button(self):
        self.wait_and_select_from_list(RentPageLocators.period_rental, RentPageLocators.day_three_period_rental)

    @allure.step('Нажатие на кнопку "Заказать"')
    def click_button_order(self):
        self.wait_and_click(RentPageLocators.button_order)

    @allure.step('Подтверждение заказа: Нажатие на кнопку "Да"')
    def click_button_order_confirmation(self):
        self.wait_and_click(RentPageLocators.button_order_confirmation)


    @allure.step('Просмотр статуса заказа: Нажатие на кнопку "Статус"')
    def click_button_status(self):
        self.wait_and_click(RentPageLocators.button_status)


    @allure.step('Обрабатываем заказ с подтверждением')
    def process_order(self, driver):
        self.click_button_order()
        browser_name = driver.capabilities['browserName'].lower()
        if browser_name != "chrome":
            self.click_button_order_confirmation()

    def wait_and_select_date(self, field_locator, date_locator, timeout=10):
        self.wait_and_click(field_locator, timeout)
        self.wait_and_click(date_locator, timeout)

    def wait_and_click(self, locator, timeout=10):
        self.wait_for(EC.element_to_be_clickable(locator), timeout).click()

    def wait_and_select_from_list(self, field_locator, option_locator, timeout=10):
        self.wait_and_click(field_locator, timeout)
        self.wait_and_click(option_locator, timeout)



