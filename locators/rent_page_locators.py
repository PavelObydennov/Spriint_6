# Здесь локаторы для второй формы заполнения
from selenium.webdriver.common.by import By


class RentPageLocators:

# Поле когда привезти самокат
    date_delivery_of_scooter = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")

# Выбираем  дату 16.01.2025
    choose_first_date_delivery_of_scooter = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='16']")

# Выбираем дату 17.01.2025
    choose_second_date_delivery_of_scooter = (By.XPATH, "//div[contains(@class, 'react-datepicker__day') and text()='17']")

# Поле срок аренды
    period_rental = [By.CLASS_NAME, 'Dropdown-control']

# Аренда на сутки
    day_one_period_rental = (By.XPATH, "//div[@aria-selected='false' and text()='сутки']")

# Аренда на 3 суток
    day_three_period_rental = (By.XPATH, "//div[@aria-selected='false' and text()='трое суток']")

# Кнопка Заказать
    button_order = (By.XPATH, "//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")

# Кнопка подтерждения заказа (да)
    button_order_confirmation = (By.XPATH, "//button[text()='Да']")

# Кнопка посмотреть статус
    button_status = (By.XPATH, "//button[text()='Посмотреть статус']")

    rent_page_next_button = (By.CLASS_NAME, 'Button_Button__ra12g ')