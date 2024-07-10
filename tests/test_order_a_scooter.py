import allure
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from pages.order_page import PagesOrder

from constants import TestUrl
from conftest import driver


class TestOrderAScooter:
    driver = None
    parametrize = 'name, surname, address, name_station, number, data, period, color, comment'
    test_data = [
        ['тестимя', 'тестфамилия', 'г.Москва', 'Черкизовская',
         89048892130, '10.08.24', 'двое суток', 'grey', 'TEST1'],
        ['тестимядва', 'тестфамилиядва', 'г.Волгоград', 'Сокольники',
         89057793440, '20.08.24', 'сутки', 'black', 'TEST2']
    ]

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get(TestUrl.BASE_URL)
        cls.page_order = PagesOrder(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    @allure.title('Заказ самоката через верхнюю кнопку')
    @allure.description('Заполняем поля и проверяем что появилось сообщение об успешном заказе')
    @pytest.mark.parametrize(f'{parametrize}', test_data)
    def test_scooter_button_up(
            self, driver, name, surname, address, name_station, number, data, period, color, comment):
        wait = WebDriverWait(driver, 10)
        self.page_order.click_up_button_order(wait)

        self.page_order.entry_fields_order(
            wait, name=name, surname=surname, address=address, name_station=name_station,
            number=number, data=data, period=period, color=color, comment=comment)
        self.page_order.check_order_success(wait)
        self.page_order.click_logo_scooter(driver, wait)
        self.page_order.check_url_after_click_logo_scooter(driver)
        self.page_order.click_logo_yandex(wait)
        self.page_order.check_url_yandex(driver, wait)

    @allure.title('Заказ самоката через нижную кнопку')
    @allure.description('Заполняем поля и проверяем что появилось сообщение об успешном заказе')
    @pytest.mark.parametrize(f'{parametrize}', test_data)
    def test_scooter_button_down(
            self, driver, name, surname, address, name_station, number, data, period, color, comment):
        wait = WebDriverWait(driver, 10)
        self.page_order.click_down_button_order(driver, wait)

        self.page_order.entry_fields_order(
            wait, name=name, surname=surname, address=address, name_station=name_station,
            number=number, data=data, period=period, color=color, comment=comment)
        self.page_order.check_order_success(wait)
        self.page_order.click_logo_scooter(driver, wait)
        self.page_order.check_url_after_click_logo_scooter(driver)
        self.page_order.click_logo_yandex(wait)
        self.page_order.check_url_yandex(driver, wait)
