from pages.base_page import BasePage
from utilities.locators import CheckoutLocators

class CheckoutPage(BasePage):
    def open_homepage(self):
        self.open("https://automationexercise.com")

    def login(self, email, password):
        self.click(CheckoutLocators.login_nav)
        self.set(CheckoutLocators.login_email, email)
        self.set(CheckoutLocators.login_password, password)
        self.click(CheckoutLocators.login_button)

    def add_product_to_cart(self, product_name):
        self.click(CheckoutLocators.add_to_cart_button(product_name))
        self.click(CheckoutLocators.view_cart_button)

    def proceed_to_checkout(self):
        self.click(CheckoutLocators.proceed_to_checkout_button)

    def review_order_and_place(self):
        self.click(CheckoutLocators.place_order_button)

    def enter_payment_details(self, name, card_number, cvc, expiry_month, expiry_year):
        self.set(CheckoutLocators.name_on_card, name)
        self.set(CheckoutLocators.card_number, card_number)
        self.set(CheckoutLocators.cvc, cvc)
        self.set(CheckoutLocators.expiry_month, expiry_month)
        self.set(CheckoutLocators.expiry_year, expiry_year)
        self.click(CheckoutLocators.pay_and_confirm_button)

    def is_order_success_message_displayed(self):
        return self.is_visible(CheckoutLocators.order_placed_message)


    def is_login_page_displayed(self):
        return self.is_visible(CheckoutLocators.login_header)
