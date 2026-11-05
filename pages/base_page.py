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

    def find_present(self, locator):
        return self.wait.until(ec.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find_clickable(locator).click()

    def type_text(self, locator, text):
        element = self.find_visible(locator)
        element.clear()
        element.send_keys(text)

    def press_key(self, locator, key):
        self.find_present(locator).send_keys(key)

    def click_if_visible(self, locator):
        elements = self.find_elements(locator)
        if elements and elements[0].is_displayed():
            elements[0].click()

    def scroll_to(self, locator):
        element = self.find_present(locator)
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

    def click_and_switch_to_new_window(self, locator):
        original_window = self.driver.current_window_handle
        self.click(locator)
        self.wait.until(ec.number_of_windows_to_be(2))
        new_window = next(
            handle
            for handle in self.driver.window_handles
            if handle != original_window
        )
        self.driver.switch_to.window(new_window)

    def wait_for_url_part(self, url_part):
        try:
            return self.wait.until(ec.url_contains(url_part))
        except TimeoutException:
            return False

    def get_current_url(self):
        return self.driver.current_url
