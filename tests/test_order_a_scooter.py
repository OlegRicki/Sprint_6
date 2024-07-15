import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from conftest import driver


class TestOrderAScooter:
    parametrize = 'name, surname, address, name_station, number, data, period, color, comment'
    test_data = [
        ['тестимя', 'тестфамилия', 'г.Москва', 'Черкизовская',
         89048892130, '10.08.24', 'двое суток', 'grey', 'TEST1'],
        ['тестимядва', 'тестфамилиядва', 'г.Волгоград', 'Сокольники',
         89057793440, '20.08.24', 'сутки', 'black', 'TEST2']
    ]

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup_class(cls, request, driver):
        cls.driver = driver

    @allure.title('Заказ самоката через верхнюю кнопку')
    @allure.description('Заполняем поля и проверяем что появилось сообщение об успешном заказе')
    @pytest.mark.parametrize(f'{parametrize}', test_data)
    def test_scooter_button_up(
            self, driver, name, surname, address, name_station, number, data, period, color, comment):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)

        main_page.click_up_button_order()

        order_page.entry_fields_order(
            name=name, surname=surname, address=address, name_station=name_station,
            number=number)
        order_page.entry_fields_rent(data=data, period=period, color=color, comment=comment)

        order_page.check_order_success()
        order_page.open_main_page()

    @allure.title('Заказ самоката через нижнюю кнопку')
    @allure.description('Заполняем поля и проверяем что появилось сообщение об успешном заказе')
    @pytest.mark.parametrize(f'{parametrize}', test_data)
    def test_scooter_button_down(
            self, driver, name, surname, address, name_station, number, data, period, color, comment):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)
        main_page.click_down_button_order()

        order_page.entry_fields_order(
            name=name, surname=surname, address=address, name_station=name_station,
            number=number)
        order_page.entry_fields_rent(data=data, period=period, color=color, comment=comment)

        order_page.check_order_success()
        order_page.open_main_page()
