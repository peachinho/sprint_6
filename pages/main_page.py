import allure
from selenium.webdriver.common.keys import Keys

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Принять сообщение о cookie, если оно показано")
    def accept_cookies(self):
        buttons = self.driver.find_elements(*MainPageLocators.COOKIE_ACCEPT_BUTTON)
        if buttons and buttons[0].is_displayed():
            buttons[0].click()

    @allure.step("Открыть форму заказа через точку входа: {entry_point}")
    def click_order_button(self, entry_point):
        locator = {
            "top_button": MainPageLocators.TOP_ORDER_BUTTON,
            "bottom_button": MainPageLocators.BOTTOM_ORDER_BUTTON,
        }[entry_point]
        self.scroll_to(locator)
        self.click(locator)

    @allure.step("Открыть вопрос FAQ с индексом {index}")
    def open_faq_question(self, index):
        locator = MainPageLocators.faq_question(index)
        question = self.scroll_to(locator)
        question.send_keys(Keys.ENTER)

    @allure.step("Получить ответ FAQ с индексом {index}")
    def get_faq_answer(self, index):
        return self.text_of(MainPageLocators.faq_answer(index))
