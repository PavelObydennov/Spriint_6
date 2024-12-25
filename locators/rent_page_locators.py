from selenium.webdriver.common.by import By

class RentPageLocators:

# Поле когда привезти самокат
    date_delivery_of_scooter = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div/div/input']

# Выбираем 1ую дату 25.12.2025
    choose_first_date_delivery_of_scooter = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[3]']

# Выбираем 2ую дату 25.12.2025
    choose_second_date_delivery_of_scooter = [By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/div[5]/div[7]']

# Поле срок аренды
    period_rental = [By.CLASS_NAME, 'Dropdown-control']

# Аренда на сутки
    day_one_period_rental = [By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div[2]/div[1]"]

# Аренда на 3 суток
    day_three_period_rental = [By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[2]/div[2]/div[3]"]

# Кнопка Заказать
    button_order = [By.XPATH, '//*[@id="root"]/div/div[2]/div[3]/button[2]']

# Кнопка подтерждения заказа (да)
    button_order_confirmation = [By.XPATH, '/html/body/div/div/div[2]/div[5]/div[2]/button[2]']

# Кнопка посмотреть статус
    button_status = [By.XPATH, '//*[@id="root"]/div/div[2]/div[5]/div[2]/button']


