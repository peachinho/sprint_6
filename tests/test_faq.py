import allure
import pytest

from data import FAQ_CASES
from pages.main_page import MainPage
from urls import BASE_URL


@allure.feature("Вопросы о важном")
class TestFaq:
    @allure.title("Ответ соответствует вопросу №{index}")
    @pytest.mark.parametrize("index, expected_answer", FAQ_CASES)
    def test_faq_answer_is_opened(self, driver, index, expected_answer):
        page = MainPage(driver, BASE_URL)
        page.open()
        page.accept_cookies()
        page.open_faq_question(index)

        assert page.get_faq_answer(index) == expected_answer

