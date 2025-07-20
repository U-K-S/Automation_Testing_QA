from pages.search_page import SearchPage

def test_search_valid_product(driver):
    page = SearchPage(driver)
    page.open_search_page()
    page.search_product("dress")
    assert page.is_search_result_displayed()  # ✅ checks actual product cards are shown

def test_search_invalid_product(driver):
    page = SearchPage(driver)
    page.open_search_page()
    page.search_product("xyz")  # unlikely to match anything
    assert page.is_no_results_message_displayed()  # ✅ checks no product cards shown
