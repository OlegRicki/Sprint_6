import allure
from faker import Faker
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time

from constants import TestUrl
from conftest import driver
from locators.main_page_locators import (MainPageLocators, OrderPageLocators, RentPageLocators, ZenPageLocators)

faker = Faker()


class PagesOrder:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликнуть на кнопку Заказать сверху страницы')
    def click_up_button_order(self, wait: WebDriverWait):
        wait.until(ec.element_to_be_clickable(MainPageLocators.BUTTON_ORDER_UP)).click()
        wait.until(ec.visibility_of_element_located(OrderPageLocators.TEXT)).is_displayed()

    @allure.step('Кликнуть на кнопку Заказать внизу страницы')
    def click_down_button_order(self, driver, wait: WebDriverWait):
        button = wait.until(ec.element_to_be_clickable(MainPageLocators.BUTTON_ORDER_DOWN))
        driver.execute_script("arguments[0].scrollIntoView(true);", button)
        button.click()
        wait.until(ec.visibility_of_element_located(OrderPageLocators.TEXT)).is_displayed()

    @allure.step('Заполнить поля ввода для заказа самоката')
    def entry_fields_order(self, wait: WebDriverWait, name: str, surname: str, address: str, name_station: str,
                           number: str, data: str, period: str, color: str, comment: str):
        # Заполнение поля имя
        field_name = wait.until(ec.element_to_be_clickable(OrderPageLocators.FIELD_NAME))
        field_name.send_keys(name)
        # Заполнение поля фамилия
        field_surname = wait.until(ec.element_to_be_clickable(OrderPageLocators.FIELD_SURNAME))
        field_surname.send_keys(surname)
        # Заолнить поле адресс
        field_address = wait.until(ec.element_to_be_clickable(OrderPageLocators.FIELD_ADDRESS))
        field_address.send_keys(address)
        # Выбор станции метро
        wait.until(ec.element_to_be_clickable(OrderPageLocators.BUTTON_METRO_STATION)).click()
        wait.until(ec.element_to_be_clickable(
            OrderPageLocators.SELECT_METRO_STATION(name_station=name_station))).click()
        # Ввод номера телефона
        field_number = wait.until(ec.element_to_be_clickable(OrderPageLocators.FIELD_NUMBER))
        field_number.send_keys(number)
        # Кликнуть на кнопку далее
        wait.until(ec.element_to_be_clickable(OrderPageLocators.BUTTON_ONWARD)).click()

        # Ввод даты
        field_rent = wait.until(ec.element_to_be_clickable(RentPageLocators.FIELD_WHEN_TO_BRING))
        field_rent.send_keys(data)
        field_rent.send_keys(Keys.ENTER)

        # Выбрать период аренды
        wait.until(ec.element_to_be_clickable(RentPageLocators.BUTTON_RENTAL_PERIOD)).click()
        wait.until(ec.visibility_of_element_located(RentPageLocators.RENTAL_PERIOD(period=period))).click()
        # Выбрать цвет
        if color:
            wait.until(ec.element_to_be_clickable(RentPageLocators.CHECKBOX_COLOR_BLACK)).click()
        else:
            wait.until(ec.element_to_be_clickable(RentPageLocators.CHECKBOX_COLOR_GREY)).click()
        # ввод комментария
        field_comment = wait.until(ec.element_to_be_clickable(RentPageLocators.FIELD_COMMENT))
        field_comment.send_keys(comment)
        # Завершить оформление заказа
        wait.until(ec.element_to_be_clickable(RentPageLocators.BUTTON_ORDER)).click()
        wait.until(ec.visibility_of_element_located(RentPageLocators.MODAL_WINDOW))
        wait.until(ec.element_to_be_clickable(RentPageLocators.BUTTON_YES)).click()

    @allure.step('Проверить отображение кнопки "Заказ оформлен"')
    def check_order_success(self, wait: WebDriverWait):
        wait.until(ec.visibility_of_element_located(RentPageLocators.ORDER_IS_PROCESSED)).is_displayed()
        wait.until(ec.element_to_be_clickable(RentPageLocators.BUTTON_SEE_STATUS)).click()

    @allure.step('Кликнуть на лого "Самокат"')
    def click_logo_scooter(self, driver, wait: WebDriverWait):
        wait.until(ec.element_to_be_clickable(MainPageLocators.BUTTON_LOGO_SCOOTER)).click()

    @allure.step('Проверить урл после клика на лого "Самокат"')
    def check_url_after_click_logo_scooter(self, driver):
        current_url = driver.current_url
        assert current_url == TestUrl.BASE_URL

    @allure.step('Клик на лого Яндекс')
    def click_logo_yandex(self, wait: WebDriverWait):
        wait.until(ec.visibility_of_element_located(MainPageLocators.BUTTON_LOGO_YANDEX))
        wait.until(ec.element_to_be_clickable(MainPageLocators.BUTTON_LOGO_YANDEX)).click()

    @allure.step('Открыть следующую  вкладку')
    def open_second_tab(self, driver):
        driver.switch_to.window(driver.window_handles[1])

    @allure.step('Проверить урл яндекс дзен')
    def check_url_yandex(self, driver, wait: WebDriverWait):

        while len(driver.window_handles) < 2:
            time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        wait.until(ec.visibility_of_element_located(ZenPageLocators.LOGO))

        current_url = driver.current_url
        assert TestUrl.BASE_YANDEX_URL == current_url
