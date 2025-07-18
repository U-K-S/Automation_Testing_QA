# tests/test_login.py

import pytest
from pages.login_page import LoginPage
from utilities.test_data import TestData

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(TestData.valid_email, TestData.valid_password)
    assert login_page.is_logged_in()

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login("wrong@example.com", "wrongpass")
    assert "Your email or password is incorrect!" in login_page.get_error_message()

def test_logout(driver):
    login_page = LoginPage(driver)
    login_page.open_login_page()
    login_page.login(TestData.valid_email, TestData.valid_password)
    assert login_page.is_logged_in()
    
    login_page.logout()
    assert "Login to your account" in driver.page_source or driver.current_url.endswith("/login")


