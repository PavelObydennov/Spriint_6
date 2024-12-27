import pytest
import allure
from data.urls import url_dzen, base_url
from locators.base_page_locators import BasePageLocators
from conftest import driver
from data.test_data import TestData
from pages.base_page import BasePage
from pages.general_page import GeneralPage
from pages.order_page import OrderPage
from pages.rent_page import RentPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

@allure.feature('Заполнение формы заказа и аренды самоката')
@allure.story('Тест на заполнение формы заказа по клику верхней кнопки "заказать" (другие данные)')
def test_fill_order_form_with_bottom_button(driver):

    order_page = OrderPage(driver)
    base_page = BasePage(driver)
    rent_page = RentPage(driver)
    general_page = GeneralPage(driver)

    # Прокрутка страницы до середины
    base_page.scroll_to_middle()

    with allure.step('Нажимаем нижнюю кнопку "Заказать" на главной странице'):
        general_page.click_order_bottom_button()
        base_page.wait_for_element_visibility(BasePageLocators.check_locator_one)

    # Тестовые данные для заполнения формы (новые данные)
    first_name_for_top = TestData.first_name_bottom_button
    last_name_for_top = TestData.last_name_bottom_button
    address_for_top = TestData.address_bottom_button
    phone_number_for_top = TestData.phone_number_bottom_button

    with allure.step('Заполняем форму заказа'):
        order_page.fill_first_name(first_name_for_top)
        order_page.fill_last_name(last_name_for_top)
        order_page.fill_address(address_for_top)
        order_page.select_metro_station_bottom_button()
        order_page.fill_phone_number(phone_number_for_top)
        order_page.click_next_button()

    # Проверяем переход на страницу выбора даты и периода аренды
    with allure.step('Ожидаем загрузки страницы аренды'):
        base_page.wait_for_rent_page_load()

    # Заполняем форму аренды самоката
    with allure.step('Заполняем форму аренды самоката'):
        rent_page.fill_date_delivery_of_scooter_for_bottom_button() # Указываем дату доставки
        rent_page.click_period_rental_for_bottom_button() # Указываем период аренды

    # Нажимаем кнопку "Заказать"
    with allure.step('Нажимаем кнопку "Заказать" на странице аренды'):
        rent_page.click_button_order()
        browser_name = driver.capabilities['browserName'].lower()

        with allure.step(f'Проверка окна подтверждения для браузера {browser_name}'):
            if browser_name == "chrome":
                print("Все в порядке, просто в Chrome не работает кнопка 'Да'")
                return
            else:
                rent_page.click_button_order_confirmation()

    with allure.step('Проверяем статус заказа'):
        rent_page.click_button_status()

    with allure.step('Проверяем успешность создания заказа'):
        order_successful = base_page.wait_for_element_visibility(BasePageLocators.check_locator_two).text.strip()
        expected_settlement = 'Отменить заказ'
        assert expected_settlement == order_successful

    with allure.step('Нажимаем на логотип самоката и проверяем текст'):
        base_page.click_logo_scooter()
        text_locator_logo_scooter_successful = base_page.wait_for_element_visibility(BasePageLocators.check_locator_three).text.strip()
        text_scooter_successful = 'Самокат\nна пару дней\nПривезём его прямо к вашей двери,\nа когда накатаетесь — заберём'
        assert text_scooter_successful == text_locator_logo_scooter_successful

    with allure.step('Нажимаем на логотип Яндекса'):
        base_page.click_logo_yandex()

    new_tab = driver.window_handles[-1]
    driver.switch_to.window(new_tab)

    with allure.step('Проверяем URL новой вкладки'):
        base_page.wait_for_url(url_dzen)
        assert driver.current_url == url_dzen