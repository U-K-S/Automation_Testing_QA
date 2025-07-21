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




class CartLocators:
    product_name = lambda name: (By.XPATH, f"//p[text()='{name}']")
    add_to_cart_button = lambda name: (By.XPATH, f"//p[text()='{name}']/following::a[text()='Add to cart'][1]")
    continue_shopping_button = (By.XPATH, "//button[text()='Continue Shopping']")
    cart_link = (By.XPATH, "//a[contains(text(),'Cart')]")
    remove_button = (By.CLASS_NAME, "cart_quantity_delete")
    view_cart_button = (By.XPATH, "//u[text()='View Cart']/parent::a")

class CheckoutLocators:
    login_nav = (By.XPATH, "//a[@href='/login']")
    login_email = (By.XPATH, "//input[@data-qa='login-email']")
    login_password = (By.XPATH, "//input[@data-qa='login-password']")
    login_button = (By.XPATH, "//button[@data-qa='login-button']")

    add_to_cart_button = lambda name: (By.XPATH, f"//p[text()='{name}']/following-sibling::a")
    view_cart_button = (By.XPATH, "//u[normalize-space()='View Cart']")
    proceed_to_checkout_button = (By.XPATH, "//a[contains(text(),'Proceed To Checkout')]")
    place_order_button = (By.XPATH, "//a[text()='Place Order']")

    name_on_card = (By.NAME, "name_on_card")
    card_number = (By.NAME, "card_number")
    cvc = (By.NAME, "cvc")
    expiry_month = (By.NAME, "expiry_month")
    expiry_year = (By.NAME, "expiry_year")
    pay_and_confirm_button = (By.ID, "submit")  # Replace with exact button locator if different

    order_placed_message = (By.XPATH, "//*[@id='form']/div/div/div/h2/b")

    login_header = (By.XPATH, "//*[contains(text(), 'Register / Login account to proceed on checkout.')]")