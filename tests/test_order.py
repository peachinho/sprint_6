import allure
import pytest

from data import ORDER_CASES
from pages.main_page import MainPage
from pages.order_page import OrderPage
from urls import BASE_URL, ORDER_URL, YANDEX_URL_PART


@allure.feature("Заказ самоката")
class TestOrder:
    @allure.title("Позитивный заказ через {entry_point}")
    @pytest.mark.parametrize("entry_point, order", ORDER_CASES)
    def test_order_can_be_created(self, driver, entry_point, order):
        main_page = MainPage(driver, BASE_URL)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_order_button(entry_point)

        order_page = OrderPage(driver, ORDER_URL)
        order_page.fill_customer_details(order)
        order_page.fill_rental_details(order)
        order_page.submit_order()

        assert order_page.is_success_modal_visible()

    @allure.title("Логотип Самоката ведёт на главную страницу")
    def test_scooter_logo_opens_home_page(self, driver):
        page = OrderPage(driver, ORDER_URL)
        page.open()
        page.click_scooter_logo()

        assert page.current_url_is(f"{BASE_URL}/")

    @allure.title("Логотип Яндекса открывает Дзен в новой вкладке")
    def test_yandex_logo_opens_dzen_in_new_tab(self, driver):
        page = OrderPage(driver, ORDER_URL, timeout=30)
        page.open()
        page.click_yandex_logo_and_switch()

        assert page.wait_for_url_part(YANDEX_URL_PART), (
            f"Ожидался редирект на {YANDEX_URL_PART}, "
            f"фактический URL: {page.get_current_url()}"
        )
