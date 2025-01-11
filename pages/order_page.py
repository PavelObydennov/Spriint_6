import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from data.urls import url_dzen, base_url

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение поля "Имя" значением: {first_name}')
    def fill_first_name(self, first_name):
        self.fill_input_field(OrderPageLocators.order_input_first_name, first_name)

    @allure.step('Заполнение поля "Фамилия" значением: {last_name}')
    def fill_last_name(self, last_name):
        self.fill_input_field(OrderPageLocators.order_input_last_name, last_name)

    @allure.step('Заполнение поля "Адрес" значением: {address}')
    def fill_address(self, address):
        self.fill_input_field(OrderPageLocators.order_input_address, address)

    @allure.step('Выбор первой станции метро из выпадающего списка (верхняя кнопка)')
    def select_metro_station_top_button(self):
        self.select_from_dropdown(
            OrderPageLocators.order_input_metro_station,
            OrderPageLocators.metro_station_first_suggestion
        )

    @allure.step('Выбор второй станции метро из выпадающего списка (нижняя кнопка)')
    def select_metro_station_bottom_button(self):
        self.select_from_dropdown(
            OrderPageLocators.order_input_metro_station,
            OrderPageLocators.metro_station_second_suggestion
        )

    @allure.step('Заполнение поля "Телефон" значением: {phone_number}')
    def fill_phone_number(self, phone_number):
        self.fill_input_field(OrderPageLocators.order_input_number_phone, phone_number)

    @allure.step('Нажатие кнопки "Далее"')
    def click_next_button(self):
        self.click_element(OrderPageLocators.order_page_locators_button_next)

    @allure.step('Заполняем форму заказа')
    def fill_order_form(self, first_name, last_name, address, phone_number):
        self.fill_first_name(first_name)
        self.fill_last_name(last_name)
        self.fill_address(address)
        self.select_metro_station_bottom_button()
        self.fill_phone_number(phone_number)
        self.click_next_button()