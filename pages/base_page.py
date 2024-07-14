from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_page(self, page):
        self.driver.get(page)

    def click_to_element(self, locator):
        self.wait.until(ec.element_to_be_clickable(locator)).click()

    def send_keys_element(self, locator, data):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        element.send_keys(data)

    def get_text_element(self, locator) -> str:
        text = self.wait.until(ec.element_to_be_clickable(locator)).text
        return text

    def check_displayed_element(self, locator):
        self.wait.until(ec.visibility_of_element_located(locator)).is_displayed()

    def scroll_to_element(self, locator):
        element = self.wait.until(ec.element_to_be_clickable(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def open_tab(self, number_tab: int):
        self.driver.switch_to.window(self.driver.window_handles[number_tab])

    def check_current_curl(self, base_url):
        current_url = self.driver.current_url
        assert current_url == base_url

    def wait_for_tab_to_page(self, number_tab: int):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > number_tab)
        self.driver.switch_to.window(self.driver.window_handles[number_tab])

    def wait_for_new_tab(self, tab_number: int):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > tab_number)

    def switch_new_tab(self, number_tab: int):
        self.driver.switch_to.window(self.driver.window_handles[number_tab])

    def close_tab(self):
        self.driver.close()



