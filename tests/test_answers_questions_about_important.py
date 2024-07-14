import allure
import pytest

from conftest import driver
from pages.main_page import MainPage
from constants import TexQuestionsAndAnswers


@pytest.fixture(scope="class")
def setup_class(request, driver):
    main_page = MainPage(driver)
    request.cls.driver = driver
    request.cls.main_page = main_page
    yield
    driver.quit()

@allure.title('Класс тестов на функционал ответов на вопросы')
@pytest.mark.usefixtures("setup_class")
class TestAnswersQuestionsAboutImportant:
    test_data = [
        [TexQuestionsAndAnswers.PRICE, TexQuestionsAndAnswers.ANSWER_PRICE],
        [TexQuestionsAndAnswers.NUMBER_OF_SCOOTER, TexQuestionsAndAnswers.ANSWER_NUMBER_OF_SCOOTER],
        [TexQuestionsAndAnswers.RENTAL_TIME, TexQuestionsAndAnswers.ANSWER_RENTAL_TIME],
        [TexQuestionsAndAnswers.ORDER_TO_DAY, TexQuestionsAndAnswers.ANSWER_ORDER_TO_DAY],
        [TexQuestionsAndAnswers.EXTEND_ORDER, TexQuestionsAndAnswers.ANSWER_EXTEND_ORDER],
        [TexQuestionsAndAnswers.CHARGING_SCOOTER, TexQuestionsAndAnswers.ANSWER_CHARGING_SCOOTER],
        [TexQuestionsAndAnswers.CANCEL_ORDER, TexQuestionsAndAnswers.ANSWER_CANCEL_ORDER],
        [TexQuestionsAndAnswers.DELIVERY_ADDRESS, TexQuestionsAndAnswers.ANSWER_DELIVERY_ADDRESS]
    ]

    @allure.title('Открыть ответы на вопросы')
    @allure.description(f'Клик на вопрос  проверяем корректный ответ')
    @pytest.mark.parametrize('question, answer', test_data)
    def test_get_answer_to_you_question(self, question, answer):
        self.main_page.click_to_question(question=question)
        text_answer = self.main_page.get_answer_to_question(question=question)
        assert text_answer == answer
