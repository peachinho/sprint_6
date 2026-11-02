from datetime import date, timedelta

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    @allure.step("Заполнить контактные данные заказчика")
    def fill_customer_details(self, order):
        self.type_text(OrderPageLocators.FIRST_NAME_INPUT, order["first_name"])
        self.type_text(OrderPageLocators.LAST_NAME_INPUT, order["last_name"])
        self.type_text(OrderPageLocators.ADDRESS_INPUT, order["address"])
        self.type_text(OrderPageLocators.METRO_INPUT, order["metro_station"])
        self.click(OrderPageLocators.metro_option(order["metro_station"]))
        self.type_text(OrderPageLocators.PHONE_INPUT, order["phone"])
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить данные об аренде")
    def fill_rental_details(self, order):
        delivery_date = (date.today() + timedelta(days=2)).strftime("%d.%m.%Y")
        date_input = self.find_visible(OrderPageLocators.DELIVERY_DATE_INPUT)
        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ESCAPE)

        self.click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click(OrderPageLocators.rental_period_option(order["rental_period"]))
        self.click(OrderPageLocators.color_checkbox(order["color"]))
        self.type_text(OrderPageLocators.COMMENT_INPUT, order["comment"])

    @allure.step("Подтвердить заказ")
    def submit_order(self):
        self.click(OrderPageLocators.ORDER_BUTTON)
        self.click(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Проверить сообщение об успешном оформлении заказа")
    def is_success_modal_visible(self):
        return self.is_visible(OrderPageLocators.SUCCESS_MODAL)

    @allure.step("Нажать логотип Самоката")
    def click_scooter_logo(self):
        self.click(OrderPageLocators.SCOOTER_LOGO)

    @allure.step("Нажать логотип Яндекса и перейти в новую вкладку")
    def click_yandex_logo_and_switch(self):
        original_window = self.driver.current_window_handle
        self.click(OrderPageLocators.YANDEX_LOGO)
        self.wait.until(ec.number_of_windows_to_be(2))
        new_window = next(
            handle for handle in self.driver.window_handles if handle != original_window
        )
        self.driver.switch_to.window(new_window)

    def wait_for_url_part(self, url_part):
        try:
            return self.wait.until(ec.url_contains(url_part))
        except TimeoutException:
            return False
