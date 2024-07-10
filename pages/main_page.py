import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver
from locators.main_page_locators import (MainPageLocators)


class MainPage:
    def __init__(self, driver):
        self.driver = driver
    @allure.step('Открыть ответ на вопрос {question}')
    def open_answer_to_question(self, driver, wait: WebDriverWait, question: str):
        element = wait.until(ec.element_to_be_clickable(MainPageLocators.CHAPTER(text_chapter=question)))
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

        wait.until(ec.element_to_be_clickable(MainPageLocators.CHAPTER(text_chapter=question))).click()

    @allure.step('Получить ответ на вопрос {question}')
    def get_answer_to_question(self, wait: WebDriverWait, question: str) -> str:
        text = wait.until(ec.visibility_of_element_located(
            MainPageLocators.ANSWER_TO_QUESTION(text_chapter=question))).text
        return text
