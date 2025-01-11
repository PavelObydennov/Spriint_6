import pytest
import allure
from data.urls import url_dzen, base_url
from conftest import driver
from data.test_data import TestData
from pages.base_page import BasePage
from pages.general_page import GeneralPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage

@allure.feature('Заполнение формы заказа и аренды самоката через верхнюю кнопку заказать')
class TestOrderFormTopButton:

    @allure.story('Тест на заполнение формы заказа по клику верхней кнопки "заказать"')
    def test_fill_order_form_with_bottom_button(self, driver):
        # Инициализация страниц
        general_page = GeneralPage(driver)
        order_page = OrderPage(driver)
        rent_page = RentPage(driver)

        # Прокрутка страницы до середины и нажатие кнопки "Заказать"
        general_page.click_order_top_button()

        # Получаем тестовые данные
        top_button_data = TestData.get_top_button_data()
        first_name = top_button_data["first_name_top_button"]
        last_name = top_button_data["last_name_top_button"]
        address = top_button_data["address_top_button"]
        phone_number = top_button_data["phone_number_top_button"]

        # Заполняем форму заказа
        order_page.fill_order_form(first_name, last_name, address, phone_number)

        # Заполняем форму аренды по дате
        rent_page.fill_date_delivery_of_scooter_for_top_button()

        # Заполняем форму аренды на кол-во дней
        rent_page.click_period_rental_for_top_button()

        # Обрабатываем заказ
        rent_page.click_button_order()

        # Проверка открытие окна
        rent_page.check_confirmation_window()

        # Нажимаем да
        rent_page.click_button_order_confirmation()

        # Нажимаем на кнопку посмотреть статус
        rent_page.click_button_status()

        # Проверяем статус заказа
        general_page.check_order_status()

        # Клик на логотип самоката
        general_page.click_logo_scooter()

        # Проверяем текст после клика на логотип самоката
        general_page.check_scooter_logo_text()

        # Проверяем URL новой вкладки после клика на логотип Яндекса
        general_page.click_logo_yandex()
        general_page.check_new_tab_url(url_dzen)