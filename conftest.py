import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--headed",
        action="store_true",
        default=False,
        help="Запустить Firefox с графическим интерфейсом",
    )


@pytest.fixture
def driver(request):
    options = Options()
    # Это решение подсказал ИИ
    options.page_load_strategy = "eager"
    if not request.config.getoption("--headed"):
        options.add_argument("-headless")

    browser = webdriver.Firefox(options=options)
    browser.set_window_size(1440, 1000)
    yield browser
    browser.quit()
