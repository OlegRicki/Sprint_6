import allure
from selenium.webdriver.support.wait import WebDriverWait

from conftest import driver
from locators.zen_page_locators import (ZenPageLocators)
from pages.base_page import BasePage
from constants import TestUrl


class ZenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step('Проверить урл яндекс дзен')
    def check_url_yandex(self):
        self.wait_for_tab_to_page(number_tab=1)
        self.wait_for_new_tab(tab_number=1)
        self.switch_new_tab(number_tab=1)
        self.check_displayed_element(locator=ZenPageLocators.LOGO)
        current_url = self.get_current_url()
        return current_url == TestUrl.BASE_YANDEX_URL

    @allure.step('Закрыть вкладку дзен и перейти на вкладку самокат')
    def close_new_tab(self):
        self.close_tab()
        self.wait_for_new_tab(tab_number=0)
