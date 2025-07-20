from pages.base_page import BasePage
from utilities.locators import SignupLocators

class SignupPage(BasePage):
    def open_signup_page(self, base_url):
        self.driver.get(base_url + "/login")

    def submit_basic_signup(self, name, email):
        self.set(SignupLocators.name_input, name)
        self.set(SignupLocators.email_input, email)
        self.click(SignupLocators.signup_button)



    def is_enter_account_info_visible(self):
        return self.is_visible(SignupLocators.enter_info_header)
    
    def fill_additional_info(self, password, day, month, year):
        self.click(SignupLocators.title_radio_mr)
        self.set(SignupLocators.password_input, password)

        self.select_dropdown(SignupLocators.dob_day, day)
        self.select_dropdown(SignupLocators.dob_month, month)
        self.select_dropdown(SignupLocators.dob_year, year)

        self.click(SignupLocators.newsletter_checkbox)
        self.click(SignupLocators.offers_checkbox)

        self.set(SignupLocators.first_name, "Test")
        self.set(SignupLocators.last_name, "User")
        self.set(SignupLocators.company, "Automation Inc.")
        self.set(SignupLocators.address1, "123 Automation St")
        self.set(SignupLocators.address2, "Suite 404")

        self.select_dropdown(SignupLocators.country, "India")

        self.set(SignupLocators.state, "Delhi")
        self.set(SignupLocators.city, "New Delhi")
        self.set(SignupLocators.zipcode, "110001")
        self.set(SignupLocators.mobile, "9876543210")

        self.click(SignupLocators.create_account_button)

