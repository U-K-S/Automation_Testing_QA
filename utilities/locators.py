# utilities/locators.py

from selenium.webdriver.common.by import By

class LoginLocators:
    email_input = (By.XPATH, "//input[@data-qa='login-email']")
    password_input = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")
    error_message = (By.XPATH, "//p[contains(text(),'incorrect')]")
    logged_in_text = (By.XPATH, "//a[contains(text(),'Logged in as')]")
    logout_button = (By.XPATH, "//a[@href='/logout']")

class SignupLocators:
    name_input = (By.NAME, "name")
    email_input = (By.XPATH, "//input[@data-qa='signup-email']")
    signup_button = (By.XPATH, "//button[text()='Signup']")
    enter_info_header = (By.XPATH, "//b[text()='Enter Account Information']")

    # --- ACCOUNT INFO ---
    title_radio_mr = (By.ID, "id_gender1")  # or adjust if needed
    password_input = (By.ID, "password")
    dob_day = (By.ID, "days")
    dob_month = (By.ID, "months")
    dob_year = (By.ID, "years")
    newsletter_checkbox = (By.ID, "newsletter")
    offers_checkbox = (By.ID, "optin")

    # --- ADDRESS INFO ---
    first_name = (By.ID, "first_name")
    last_name = (By.ID, "last_name")
    company = (By.ID, "company")
    address1 = (By.ID, "address1")
    address2 = (By.ID, "address2")
    country = (By.ID, "country")
    state = (By.ID, "state")
    city = (By.ID, "city")
    zipcode = (By.ID, "zipcode")
    mobile = (By.ID, "mobile_number")

    create_account_button = (By.XPATH, "//button[text()='Create Account']")
    account_created_message = (By.XPATH, "//b[text()='Account Created!']")

class SearchLocators:
    search_input = (By.ID, "search_product")
    search_button = (By.ID, "submit_search")
