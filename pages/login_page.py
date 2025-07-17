# pages/login_page.py

from pages.base_page import BasePage
from utilities.locators import LoginLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email, password):
        self.set(LoginLocators.email_input, email)
        self.set(LoginLocators.password_input, password)
        self.click(LoginLocators.login_button)
