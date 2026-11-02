from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Адрес: куда привезти заказ']",
    )
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Телефон: на него позвонит курьер']",
    )
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DELIVERY_DATE_INPUT = (
        By.XPATH,
        "//input[@placeholder='* Когда привезти самокат']",
    )
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Buttons')]//button[text()='Заказать']",
    )
    CONFIRM_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Order_Modal')]//button[text()='Да']",
    )
    SUCCESS_MODAL = (
        By.XPATH,
        "//div[contains(@class, 'Order_ModalHeader') and "
        "contains(., 'Заказ оформлен')]",
    )

    SCOOTER_LOGO = (By.CSS_SELECTOR, "a[class*='Header_LogoScooter']")
    YANDEX_LOGO = (By.CSS_SELECTOR, "a[class*='Header_LogoYandex']")

    @staticmethod
    def metro_option(station):
        return By.XPATH, f"//button[normalize-space()='{station}']"

    @staticmethod
    def rental_period_option(period):
        return By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']"

    @staticmethod
    def color_checkbox(color):
        return By.ID, color

