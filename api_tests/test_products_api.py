import requests

BASE_URL = "https://automationexercise.com/api"

def test_get_all_products():
    """
    Test to verify that the GET /productsList API returns 200 OK
    and includes a non-empty list of products.
    """
    response = requests.get(f"{BASE_URL}/productsList")
    
    # Assert status code
    assert response.status_code == 200, "Expected status code 200"

    # Parse JSON response
    response_json = response.json()
    
    # Assert products key exists
    assert "products" in response_json, "Response should contain 'products' key"
    
    # Assert products list is not empty
    assert len(response_json["products"]) > 0, "Product list should not be empty"

def test_post_search_product():
    """
    Test to verify that the POST /searchProduct API returns
    results for a valid search keyword, and at least one
    result is relevant to the search term.
    """
    payload = {
        "search_product": "top"
    }

    response = requests.post(f"{BASE_URL}/searchProduct", data=payload)

    # Assert status code
    assert response.status_code == 200, "Expected status code 200"

    # Parse JSON
    response_json = response.json()

    # Assert 'products' key exists
    assert "products" in response_json, "'products' key not in response"

    # Assert product list is not empty
    assert len(response_json["products"]) > 0, "No products returned for search"

    # Check if at least one product name contains the search keyword
    relevant = any("top" in product.get("name", "").lower() for product in response_json["products"])
    assert relevant, "No product name contains the word 'top'"
