import pytest
import random
from pages.signup_page import SignupPage
from utilities.test_data import TestData
from utilities.locators import SignupLocators

def generate_random_email():
    return f"user{random.randint(10000, 99999)}@test.com"

def test_full_signup_flow(driver):
    page = SignupPage(driver)
    page.open_signup_page(TestData.base_url)

    name = "Test User"
    email = generate_random_email()
    page.submit_basic_signup(name, email)

    # Assert that 'Enter Account Information' header is visible
    assert page.is_visible(SignupLocators.enter_info_header)

    # Fill full signup form
    page.fill_additional_info(
        password="TestPass123",
        day="10",
        month="May",
        year="1995"
    )

    # Assert account created message is shown
    assert page.is_visible(SignupLocators.account_created_message)
