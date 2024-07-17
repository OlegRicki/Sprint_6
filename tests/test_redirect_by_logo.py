import allure

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.zen_page import ZenPage
from conftest import driver


class TestRedirectByLogo:

    @allure.title('Тест перенаправление на главную страницу, после клика на лого "Самокат" ')
    @allure.description('Переход на любую страницу(кроме главной),'
                        ' клик на лого самокат, проверяем открытие главной страницы')
    def test_redirect_by_logo_scooter(self, driver):
        order_page = OrderPage(driver)
        main_page = MainPage(driver)

        main_page.click_up_button_order()
        main_page.click_logo_scooter()
        assert order_page.check_url_after_click_logo_scooter()
        order_page.open_main_page()

    @allure.title('Тест перенаправление на страницу дзена, после клика на лого "Яндекс" ')
    @allure.description('Клик на лого Яндекс, проверяем открытие страницы яндекса')
    def test_redirect_by_logo_yandex(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        zen_page = ZenPage(driver)

        main_page.click_logo_yandex()
        assert zen_page.check_url_yandex()
        order_page.open_main_page()
