import allure
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Кликнуть на вопрос {question}')
    def click_to_question(self, question: str):
        self.scroll_to_element(locator=MainPageLocators.CHAPTER(text_chapter=question))
        self.click_to_element(locator=MainPageLocators.CHAPTER(text_chapter=question))

    @allure.step('Получить ответ на вопрос {question}')
    def get_answer_to_question(self, question: str) -> str:
        text = self.get_text_element(locator=MainPageLocators.ANSWER_TO_QUESTION(text_chapter=question))
        return text

    @allure.step('Кликнуть на кнопку Заказать сверху страницы')
    def click_up_button_order(self):
        self.click_to_element(locator=MainPageLocators.BUTTON_ORDER_UP)

    @allure.step('Кликнуть на кнопку Заказать внизу страницы')
    def click_down_button_order(self):
        self.scroll_to_element(locator=MainPageLocators.BUTTON_ORDER_DOWN)
        self.click_to_element(locator=MainPageLocators.BUTTON_ORDER_DOWN)

    @allure.step('Кликнуть на лого "Самокат"')
    def click_logo_scooter(self):
        self.click_to_element(locator=MainPageLocators.BUTTON_LOGO_SCOOTER)

    @allure.step('Клик на лого Яндекс')
    def click_logo_yandex(self):
        self.check_displayed_element(locator=MainPageLocators.BUTTON_LOGO_YANDEX)
        self.click_to_element(locator=MainPageLocators.BUTTON_LOGO_YANDEX)
