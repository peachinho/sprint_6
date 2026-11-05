from datetime import date, timedelta

import allure
from selenium.webdriver.common.keys import Keys

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
        self.type_text(OrderPageLocators.DELIVERY_DATE_INPUT, delivery_date)
        self.press_key(OrderPageLocators.DELIVERY_DATE_INPUT, Keys.ESCAPE)

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
        self.click_and_switch_to_new_window(OrderPageLocators.YANDEX_LOGO)
