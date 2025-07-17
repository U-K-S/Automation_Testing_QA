# tests/test_login.py

import pytest
from pages.login_page import LoginPage
from utilities.test_data import TestData

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open(TestData.base_url + "/login")
    login_page.login(TestData.valid_email, TestData.valid_password)
    assert "Logged in as" in driver.page_source
