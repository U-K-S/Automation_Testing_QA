from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from utilities.test_data import TestData
from utilities.locators import CartLocators
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    def open_product_page(self):
        self.driver.get(TestData.base_url + "/products")

    def add_product_to_cart(self, product_name):
        locator = CartLocators.add_to_cart_button(product_name)

        # Scroll to and click the Add to Cart button
        button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        button.click()

        # Wait for modal and click 'View Cart'
        view_cart_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(CartLocators.view_cart_button)
        )
        view_cart_btn.click()


    def open_cart(self):
        self.click(CartLocators.cart_link)
        time.sleep(1)

    def is_product_in_cart(self, product_name):
        return product_name.lower() in self.driver.page_source.lower()

    def remove_product_from_cart(self, product_name):
        self.click(CartLocators.remove_button)
        time.sleep(1)

    def is_cart_empty(self):
        return "Cart is empty!" in self.driver.page_source
