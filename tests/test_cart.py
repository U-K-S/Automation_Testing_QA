from pages.cart_page import CartPage

def test_add_product_to_cart(driver):
    page = CartPage(driver)
    page.open_product_page()
    page.add_product_to_cart("Blue Top")
    page.open_cart()
    assert page.is_product_in_cart("Blue Top")

def test_remove_product_from_cart(driver):
    page = CartPage(driver)
    page.open_product_page()
    page.add_product_to_cart("Blue Top")
    page.open_cart()
    page.remove_product_from_cart("Blue Top")
    assert page.is_cart_empty()
