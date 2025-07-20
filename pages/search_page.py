from pages.base_page import BasePage
from utilities.locators import SearchLocators
from utilities.test_data import TestData
from selenium.webdriver.common.by import By  # ✅ Add this line

class SearchPage(BasePage):
    def open_search_page(self):
        self.driver.get(TestData.base_url + "/products")

    def search_product(self, keyword):
        self.set(SearchLocators.search_input, keyword)
        self.click(SearchLocators.search_button)

    def is_search_result_displayed(self):
        products = self.driver.find_elements(By.CLASS_NAME, "productinfo")
        return len(products) > 0

    def is_no_results_message_displayed(self):
        products = self.driver.find_elements(By.CLASS_NAME, "productinfo")
        return len(products) == 0
