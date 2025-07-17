# pages/login_page.py

from pages.base_page import BasePage
from utilities.locators import LoginLocators
from utilities.test_data import TestData

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.open(TestData.base_url + "/login")

    def login(self, email, password):
        self.set(LoginLocators.email_input, email)
        self.set(LoginLocators.password_input, password)
        self.click(LoginLocators.login_button)

    def get_error_message(self):
        return self.get_text(LoginLocators.error_message)

    def is_logged_in(self):
        return self.is_visible(LoginLocators.logged_in_text)
