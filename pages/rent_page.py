import allure
from pages.base_page import BasePage
from locators.rent_page_locators import RentPageLocators
from data.urls import url_dzen, base_url

class RentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Выбор даты доставки самоката на 16 января 2025')
    def fill_date_delivery_of_scooter_for_top_button(self):
        self.select_date(
            RentPageLocators.date_delivery_of_scooter,
            RentPageLocators.choose_first_date_delivery_of_scooter
        )

    @allure.step('Выбор даты доставки самоката на 17 января 2025')
    def fill_date_delivery_of_scooter_for_bottom_button(self):
        self.select_date(
            RentPageLocators.date_delivery_of_scooter,
            RentPageLocators.choose_second_date_delivery_of_scooter
        )

    @allure.step('Выбор срока аренды на сутки')
    def click_period_rental_for_top_button(self):
        self.select_from_dropdown_list(
            RentPageLocators.period_rental,
            RentPageLocators.day_one_period_rental
        )

    @allure.step('Выбор срока аренды на трое суток')
    def click_period_rental_for_bottom_button(self):
        self.select_from_dropdown_list(
            RentPageLocators.period_rental,
            RentPageLocators.day_three_period_rental
        )

    @allure.step('Нажатие на кнопку "Заказать"')
    def click_button_order(self):
        self.click_element(RentPageLocators.button_order)

    @allure.step('Подтверждение заказа: Нажатие на кнопку "Да"')
    def click_button_order_confirmation(self):
        self.click_element(RentPageLocators.button_order_confirmation)

    @allure.step('Просмотр статуса заказа: Нажатие на кнопку "Статус"')
    def click_button_status(self):
        self.click_element(RentPageLocators.button_status)

    @allure.step('Обрабатываем заказ с подтверждением')
    def process_order(self):
        self.click_button_order()
        browser_name = self.get_browser_name()
        if browser_name != "chrome":
            self.click_button_order_confirmation()



