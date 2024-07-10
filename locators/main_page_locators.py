from selenium.webdriver.common.by import By


class MainPageLocators:
    CHAPTER = lambda **v: (By.XPATH, '//div[text()="{text_chapter}"]'.format(**v))
    ANSWER_TO_QUESTION = lambda **v: (
        By.XPATH, '//div[text()="{text_chapter}"]/../..//div[@class="accordion__panel"]'.format(**v))

    BUTTON_ORDER_UP = (By.XPATH, '(//button[text()="Заказать"])[1]')
    BUTTON_ORDER_DOWN = (By.XPATH, '(//button[text()="Заказать"])[2]')
    BUTTON_LOGO_SCOOTER = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')
    BUTTON_LOGO_YANDEX = (By.XPATH, '//a[contains(@class, "_LogoYandex")]')


class OrderPageLocators:
    TEXT = (By.XPATH, '//div[text()="Для кого самокат"]')
    FIELD_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')
    FIELD_SURNAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    FIELD_ADDRESS = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    BUTTON_METRO_STATION = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    SELECT_METRO_STATION = lambda **v: (By.XPATH, '(//div[text()="{name_station}"])[1]'.format(**v))
    FIELD_NUMBER = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    BUTTON_ONWARD = (By.XPATH, '//button[text()="Далее"]')


class RentPageLocators:
    FIELD_WHEN_TO_BRING = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    BUTTON_RENTAL_PERIOD = (By.XPATH, '//div[text()="* Срок аренды"]')
    RENTAL_PERIOD = lambda **v: (By.XPATH, '//div[@class="Dropdown-menu"]//div[text()="{period}"]'.format(**v))
    CHECKBOX_COLOR_BLACK = (By.XPATH, '//input[@id="black"]')
    CHECKBOX_COLOR_GREY = (By.XPATH, '//input[@id="grey"]')
    FIELD_COMMENT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    BUTTON_YES = (By.XPATH, '//button[text()="Да"]')
    BUTTON_ORDER = (By.XPATH, '(//button[text()="Заказать"])[2]')
    MODAL_WINDOW = (By.XPATH, '//div[contains(@class, "Order_Modal_")]')
    ORDER_IS_PROCESSED = (By.XPATH, '//div[text()="Заказ оформлен"]')
    BUTTON_SEE_STATUS = (By.XPATH, '//button[text()="Посмотреть статус"]')


class ZenPageLocators:
    LOGO = (By.XPATH, '//a[@aria-label="Логотип Бренда"]')
