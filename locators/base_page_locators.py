from selenium.webdriver.common.by import By


class BasePageLocators:
# Локатор верхней кнопки "Заказать"
    order_top_button = [By.CLASS_NAME, 'Button_Button__ra12g']
# Локатор логотипа "Самокат"
    logo_scooter = [By.CLASS_NAME,'Header_LogoScooter__3lsAR']
# Локатор логотипа "Яндекс"
    logo_Yandex = [By.CLASS_NAME,'Header_LogoYandex__3TSOI']

    check_locator_one = (By.CSS_SELECTOR, ".Order_Header__BZXOb")

    check_locator_two = (By.CSS_SELECTOR, ".Button_Button__ra12g.Button_Inverted__3IF-i")

    check_locator_three = (By.CLASS_NAME, 'Home_Header__iJKdX')
