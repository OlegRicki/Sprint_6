import allure
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from constants import TexQuestionsAndAnswers
from pages.main_page import MainPage


class TestAnswersQuestionsAboutImportant:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.main_page = MainPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('Открыть ответы на вопросы')
    @allure.description(f'Клик на вопрос  проверяем корректный ответ')
    def test_open_question_price(self, driver):
        question = TexQuestionsAndAnswers.PRICE
        answer = TexQuestionsAndAnswers.ANSWER_PRICE
        wait = WebDriverWait(driver, 10)
        self.main_page.open_answer_to_question(driver, wait, question=question)
        text_answer = self.main_page.get_answer_to_question(wait, question=question)
        assert text_answer == answer

    @allure.title('Открыть ответы на вопросы')
    @allure.description(f'Клик на вопрос  проверяем корректный ответ')
    def test_open_question_number_of_scooter(self, driver):
        question = TexQuestionsAndAnswers.NUMBER_OF_SCOOTER
        answer = TexQuestionsAndAnswers.ANSWER_NUMBER_OF_SCOOTER
        wait = WebDriverWait(driver, 10)
        self.main_page.open_answer_to_question(driver, wait, question=question)
        text_answer = self.main_page.get_answer_to_question(wait, question=question)
        assert text_answer == answer

    @allure.title('Открыть ответы на вопросы')
    @allure.description(f'Клик на вопрос  проверяем корректный ответ')
    def test_open_question_rental_time(self, driver):
        question = TexQuestionsAndAnswers.RENTAL_TIME
        answer = TexQuestionsAndAnswers.ANSWER_RENTAL_TIME
        wait = WebDriverWait(driver, 10)
        self.main_page.open_answer_to_question(driver, wait, question=question)
        text_answer = self.main_page.get_answer_to_question(wait, question=question)
        assert text_answer == answer

    @allure.title('Открыть ответы на вопросы')
    @allure.description(f'Клик на вопрос  проверяем корректный ответ')
    def test_open_question_order_to_day(self, driver):
        question = TexQuestionsAndAnswers.ORDER_TO_DAY
        answer = TexQuestionsAndAnswers.ANSWER_ORDER_TO_DAY
        wait = WebDriverWait(driver, 10)
        self.main_page.open_answer_to_question(driver, wait, question=question)
        text_answer = self.main_page.get_answer_to_question(wait, question=question)
        assert text_answer == answer

    @allure.title('Открыть ответы на вопросы')
    @allure.description(f'Клик на вопрос  проверяем корректный ответ')
    def test_open_question_extend_order(self, driver):
        question = TexQuestionsAndAnswers.EXTEND_ORDER
        answer = TexQuestionsAndAnswers.ANSWER_EXTEND_ORDER
        wait = WebDriverWait(driver, 10)
        self.main_page.open_answer_to_question(driver, wait, question=question)
        text_answer = self.main_page.get_answer_to_question(wait, question=question)

        assert text_answer == answer

    @allure.title('Открыть ответы на вопросы')
    @allure.description(f'Клик на вопрос  проверяем корректный ответ')
    def test_open_question_charging(self, driver):
        question = TexQuestionsAndAnswers.CHARGING_SCOOTER
        answer = TexQuestionsAndAnswers.ANSWER_CHARGING_SCOOTER
        wait = WebDriverWait(driver, 10)
        self.main_page.open_answer_to_question(driver, wait, question=question)
        text_answer = self.main_page.get_answer_to_question(wait, question=question)
        assert text_answer == answer

    @allure.title('Открыть ответы на вопросы')
    @allure.description(f'Клик на вопрос  проверяем корректный ответ')
    def test_open_question_cancel_order(self, driver):
        question = TexQuestionsAndAnswers.CANCEL_ORDER
        answer = TexQuestionsAndAnswers.ANSWER_CANCEL_ORDER
        wait = WebDriverWait(driver, 10)
        self.main_page.open_answer_to_question(driver, wait, question=question)
        text_answer = self.main_page.get_answer_to_question(wait, question=question)
        assert text_answer == answer

    @allure.title('Открыть ответы на вопросы')
    @allure.description(f'Клик на вопрос  проверяем корректный ответ')
    def test_open_question_delivery_address(self, driver):
        question = TexQuestionsAndAnswers.DELIVERY_ADDRESS
        answer = TexQuestionsAndAnswers.ANSWER_DELIVERY_ADDRESS
        wait = WebDriverWait(driver, 10)
        self.main_page.open_answer_to_question(driver, wait, question=question)
        text_answer = self.main_page.get_answer_to_question(wait, question=question)
        assert text_answer == answer
