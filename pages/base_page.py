import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self, driver, url, timeout=45):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Открыть страницу")
    def open(self):
        self.driver.get(self.url)

    def find_visible(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def scroll_to(self, locator):
        element = self.wait.until(ec.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", element
        )
        return element

    def text_of(self, locator):
        return self.find_visible(locator).text

    def is_visible(self, locator):
        try:
            self.find_visible(locator)
            return True
        except TimeoutException:
            return False

    def current_url_is(self, expected_url):
        return self.wait.until(ec.url_to_be(expected_url))
