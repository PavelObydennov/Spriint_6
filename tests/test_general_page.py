import pytest
import allure
from conftest import driver
from pages.base_page import BasePage
from pages.general_page import GeneralPage
from selenium.webdriver.support.ui import WebDriverWait
from locators.general_page_locators import GeneralPageLocators
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.parametrize(
    "question_method, answer_locator, expected_answer",
    [
        ('click_question_one', GeneralPageLocators.answer_one, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        ('click_question_two', GeneralPageLocators.answer_two, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        ('click_question_three', GeneralPageLocators.answer_three, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        ('click_question_four', GeneralPageLocators.answer_four, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        ('click_question_five', GeneralPageLocators.answer_five, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        ('click_question_six', GeneralPageLocators.answer_six, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        ('click_question_seven', GeneralPageLocators.answer_seven, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        ('click_question_eight', GeneralPageLocators.answer_eight, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ]
)
@allure.title('Тест клика по вопросам и проверки ответов')
def test_click_question(driver, question_method, answer_locator, expected_answer):
    general_page = GeneralPage(driver)
    general_page.scroll_to_bottom()

    with allure.step(f'Клик по вопросу: {question_method}'):
        getattr(general_page, question_method)()

    actually_settlement = general_page.wait_for_element(answer_locator).text.strip()

    with allure.step('Проверка текста ответа'):
        assert expected_answer == actually_settlement