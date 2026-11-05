from selenium.webdriver.common.by import By


class MainPageLocators:
    COOKIE_ACCEPT_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    TOP_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[1]")
    BOTTOM_ORDER_BUTTON = (By.XPATH, "(//button[text()='Заказать'])[2]")
    FAQ_SECTION = (By.XPATH, "//*[text()='Вопросы о важном']")

    @staticmethod
    def faq_question(index):
        return By.ID, f"accordion__heading-{index}"

    @staticmethod
    def faq_answer(index):
        return By.ID, f"accordion__panel-{index}"

