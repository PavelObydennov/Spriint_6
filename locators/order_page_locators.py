# Здесь хранятся локаторы страницы оформления заказа.
from selenium.webdriver.common.by import By



class OrderPageLocators:
# Локаторы полей для ввода данных о пользователе.
    order_input_first_name = [By.XPATH, "//input[@placeholder='* Имя']"] # Поле Имя
    order_input_last_name = [By.XPATH, "//input[@placeholder='* Фамилия']"] # Поле Фамилия
    order_input_address = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"] # Поле Адрес
    order_input_metro_station = (By.XPATH, "//input[@placeholder='* Станция метро']") # Поле станция метро
    metro_station_first_suggestion = (By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li[1]") # Первый пункт станции метро
    metro_station_second_suggestion = (By.XPATH, "//div[contains(@class, 'select-search__select')]/ul/li[2]") # Первый пункт станции метро
    order_input_number_phone = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"] # Поле номер телефона

# Локатор кнопки "далее" для оформления заказа.
    order_page_locators_button_next = (By.XPATH,"//*[@id='root']/div/div[2]/div[3]/button")

