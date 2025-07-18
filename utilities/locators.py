# utilities/locators.py

from selenium.webdriver.common.by import By

class LoginLocators:
    email_input = (By.XPATH, "//input[@data-qa='login-email']")
    password_input = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")
    error_message = (By.XPATH, "//p[contains(text(),'incorrect')]")
    logged_in_text = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    logout_button = (By.XPATH, "//a[@href='/logout']")