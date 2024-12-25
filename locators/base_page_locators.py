from selenium.webdriver.common.by import By


class BasePageLocators:

# Локатор верхней кнопки "Заказать"
    order_top_button = [By.CLASS_NAME, 'Button_Button__ra12g']

# Локатор логотипа "Самокат"
    logo_scooter = [By.CLASS_NAME,'Header_LogoScooter__3lsAR']

# Локатор логотипа "Яндекс"
    logo_Yandex = [By.CLASS_NAME,'Header_LogoYandex__3TSOI']