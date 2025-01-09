import pytest
import allure
from conftest import driver
from pages.general_page import GeneralPage
from locators.general_page_locators import GeneralPageLocators

@allure.feature('Проверка работоспособности кнопок "Вопросы о важном"')
class TestGeneralPage:
    @pytest.mark.parametrize(
        "question_locator, answer_locator, expected_answer",
        [
            (GeneralPageLocators.question_one, GeneralPageLocators.answer_one, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
            (GeneralPageLocators.question_two, GeneralPageLocators.answer_two, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
            (GeneralPageLocators.question_three, GeneralPageLocators.answer_three, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
            (GeneralPageLocators.question_four, GeneralPageLocators.answer_four, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
            (GeneralPageLocators.question_five, GeneralPageLocators.answer_five, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
            (GeneralPageLocators.question_six, GeneralPageLocators.answer_six, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
            (GeneralPageLocators.question_seven, GeneralPageLocators.answer_seven, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
            (GeneralPageLocators.question_eight, GeneralPageLocators.answer_eight, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
        ]
    )
    @allure.title('Тест клика по вопросам и проверки ответов')
    def test_click_question(self, driver, question_locator, answer_locator, expected_answer):
        # Инициализация страницы
        general_page = GeneralPage(driver)

        # Скроллим к элементу вопроса
        general_page.scroll_to_bottom()

        # Нажимаем на вопрос
        general_page.click_question(question_locator)

        # Проверяем, что ответ стал видимым
        actual_answer = general_page.get_element_text(answer_locator)
        assert actual_answer == expected_answer