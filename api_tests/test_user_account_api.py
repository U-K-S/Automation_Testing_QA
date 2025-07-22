import requests

BASE_URL = "https://automationexercise.com/api"

def test_get_user_details_by_email():
    """
    Test to verify that GET /getUserDetailByEmail returns correct
    user details when a valid email is provided.
    """

    test_email = "utksh0308@gmail.com"  # Use a valid, created email

    response = requests.get(f"{BASE_URL}/getUserDetailByEmail?email={test_email}")

    assert response.status_code == 200, "Expected status code 200"

    response_json = response.json()

    assert response_json.get("responseCode") == 200, "Failed to retrieve user details"
    assert "user" in response_json, "'user' key not found in response"
    assert response_json["user"].get("email") == test_email, "Email mismatch in response"
