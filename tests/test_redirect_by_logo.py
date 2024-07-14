import allure
import pytest

from pages.main_page import MainPage
from pages.order_page import OrderPage
from pages.zen_page import ZenPage
from conftest import driver


@pytest.fixture(scope="class")
def setup_class(request, driver):
    order_page = OrderPage(driver)
    request.cls.driver = driver
    request.cls.order_page = order_page

    main_page = MainPage(driver)
    request.cls.driver = driver
    request.cls.main_page = main_page

    zen_page = ZenPage(driver)
    request.cls.driver = driver
    request.cls.zen_page = zen_page
    yield
    driver.quit()


@pytest.mark.usefixtures("setup_class")
class TestRedirectByLogo:

    def setup_method(self, method):
        self.order_page.open_main_page()

    @allure.title('Тест перенаправление на главную страницу, после клика на лого "Самокат" ')
    @allure.description('Переход на любую страницу(кроме главной),'
                        ' клик на лого самокат, проверяем открытие главной страницы')
    def test_redirect_by_logo_scooter(self):
        self.main_page.click_up_button_order()
        self.main_page.click_logo_scooter()
        self.order_page.check_url_after_click_logo_scooter()

    @allure.title('Тест перенаправление на страницу дзена, после клика на лого "Яндекс" ')
    @allure.description('Клик на лого Яндекс, проверяем открытие страницы яндекса')
    def test_redirect_by_logo_yandex(self):
        self.main_page.click_logo_yandex()
        self.zen_page.check_url_yandex()
