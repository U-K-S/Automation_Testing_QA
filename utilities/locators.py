# utilities/locators.py

from selenium.webdriver.common.by import By

class LoginLocators:
    email_input = (By.NAME, "email")
    password_input = (By.NAME, "password")
    login_button = (By.XPATH, "//button[text()='Login']")
