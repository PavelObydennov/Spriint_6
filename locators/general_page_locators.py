# Здесь хранятся локаторы главной страницы.
from selenium.webdriver.common.by import By



class GeneralPageLocators:
    # Локатор нижней кнопки "Заказать"
    order_bottom_button = (By.XPATH, '//*[@id="root"]/div/div/div[4]/div[2]/div[5]/button')

    # Вопросы выпадающего списка в разделе «Вопросы о важном»
    question_one = (By.ID, 'accordion__heading-0')
    question_two = (By.ID, 'accordion__heading-1')
    question_three = (By.ID, 'accordion__heading-2')
    question_four = (By.ID, 'accordion__heading-3')
    question_five = (By.ID, 'accordion__heading-4')
    question_six = (By.ID, 'accordion__heading-5')
    question_seven = (By.ID, 'accordion__heading-6')
    question_eight = (By.ID, 'accordion__heading-7')

    # Ответы на вопросы выпадающего списка в разделе «Вопросы о важном»
    answer_one = (By.ID, 'accordion__panel-0')
    answer_two = (By.ID, 'accordion__panel-1')
    answer_three = (By.ID, 'accordion__panel-2')
    answer_four = (By.ID, 'accordion__panel-3')
    answer_five = (By.ID, 'accordion__panel-4')
    answer_six = (By.ID, 'accordion__panel-5')
    answer_seven = (By.ID, 'accordion__panel-6')
    answer_eight = (By.ID, 'accordion__panel-7')


