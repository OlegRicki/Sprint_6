import allure
from selenium.webdriver.support.wait import WebDriverWait
from conftest import driver
from locators.order_page_locators import (OrderPageLocators)
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from constants import TestUrl


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    @allure.step(f'Открыть страницу {TestUrl.BASE_URL}')
    def open_main_page(self):
        self.open_page(page=TestUrl.BASE_URL)

    @allure.step('Заполнить поля ввода для заказа самоката')
    def entry_fields_order(self, name: str, surname: str, address: str, name_station: str,
                           number: str):
        # Заполнение поля имя
        self.send_keys_element(locator=OrderPageLocators.FIELD_NAME, data=name)
        # Заполнение поля фамилия
        self.send_keys_element(locator=OrderPageLocators.FIELD_SURNAME, data=surname)
        # Заолнить поле адресс
        self.send_keys_element(locator=OrderPageLocators.FIELD_ADDRESS, data=address)
        # Выбор станции метро
        self.click_to_element(locator=OrderPageLocators.BUTTON_METRO_STATION)
        self.click_to_element(locator=OrderPageLocators.SELECT_METRO_STATION(name_station=name_station))
        # Ввод номера телефона
        self.send_keys_element(locator=OrderPageLocators.FIELD_NUMBER, data=number)

        # Кликнуть на кнопку далее
        self.click_to_element(locator=OrderPageLocators.BUTTON_ONWARD)

    @allure.step('Заполнить поля аренды')
    def entry_fields_rent(self, data: str, period: str, color: str, comment: str):
        # Ввод даты
        self.send_keys_element(locator=OrderPageLocators.FIELD_WHEN_TO_BRING, data=data)
        self.send_keys_element(locator=OrderPageLocators.FIELD_WHEN_TO_BRING, data=Keys.ENTER)

        # Выбрать период аренды
        self.click_to_element(locator=OrderPageLocators.BUTTON_RENTAL_PERIOD)
        self.click_to_element(locator=OrderPageLocators.RENTAL_PERIOD(period=period))

        # Выбрать цвет
        if color:
            self.click_to_element(locator=OrderPageLocators.CHECKBOX_COLOR_BLACK)
        else:
            self.click_to_element(locator=OrderPageLocators.CHECKBOX_COLOR_GREY)

        # ввод комментария
        self.send_keys_element(locator=OrderPageLocators.FIELD_COMMENT, data=comment)
        # Завершить оформление заказа
        self.click_to_element(locator=OrderPageLocators.BUTTON_ORDER)
        self.check_displayed_element(locator=OrderPageLocators.MODAL_WINDOW)
        self.click_to_element(locator=OrderPageLocators.BUTTON_YES)

    @allure.step('Проверить отображение кнопки "Заказ оформлен"')
    def check_order_success(self):
        self.check_displayed_element(locator=OrderPageLocators.ORDER_IS_PROCESSED)
        self.click_to_element(locator=OrderPageLocators.BUTTON_SEE_STATUS)

    @allure.step('Проверить урл после клика на лого "Самокат"')
    def check_url_after_click_logo_scooter(self):
        self.check_current_curl(TestUrl.BASE_URL)
