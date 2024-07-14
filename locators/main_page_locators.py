from selenium.webdriver.common.by import By


class MainPageLocators:
    CHAPTER = lambda **v: (By.XPATH, '//div[text()="{text_chapter}"]'.format(**v))
    ANSWER_TO_QUESTION = lambda **v: (
        By.XPATH, '//div[text()="{text_chapter}"]/../..//div[@class="accordion__panel"]'.format(**v))

    BUTTON_ORDER_UP = (By.XPATH, '(//button[text()="Заказать"])[1]')
    BUTTON_ORDER_DOWN = (By.XPATH, '(//button[text()="Заказать"])[2]')
    BUTTON_LOGO_SCOOTER = (By.XPATH, '//a[contains(@class, "Header_LogoScooter")]')
    BUTTON_LOGO_YANDEX = (By.XPATH, '//a[contains(@class, "_LogoYandex")]')
    QUESTIONS_ABOUT_IMPORTANT = (By.XPATH, '//div[text()="Вопросы о важном"]')
