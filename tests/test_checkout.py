import pytest
from pages.checkout_page import CheckoutPage
from utilities.test_data import TestData

def test_valid_checkout_after_login(driver):
    page = CheckoutPage(driver)
    page.open_homepage()
    page.login(TestData.valid_email, TestData.valid_password)

    page.add_product_to_cart("Blue Top")
    page.proceed_to_checkout()
    page.review_order_and_place()
    page.enter_payment_details(
        name="Test User",
        card_number="4111111111111111",
        cvc="123",
        expiry_month="12",
        expiry_year="2025"
    )

    assert page.is_order_success_message_displayed()


def test_checkout_without_login(driver):
    page = CheckoutPage(driver)
    page.open_homepage()
    page.add_product_to_cart("Blue Top")
    page.proceed_to_checkout()

    # Assert user is redirected to login/signup page
    assert page.is_login_page_displayed()
