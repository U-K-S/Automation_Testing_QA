import requests

BASE_URL = "https://automationexercise.com/api"

def test_verify_login_valid_credentials():
    """
    Test to verify that the POST /verifyLogin API authenticates a user
    correctly with valid email and password.
    """

    payload = {
        "email": "utksh0308@gmail.com",
        "password": "123"
    }

    response = requests.post(f"{BASE_URL}/verifyLogin", data=payload)

    # Assert status code
    assert response.status_code == 200, "Expected status code 200"

    # Assert response JSON
    response_json = response.json()

    assert response_json.get("responseCode") == 200, "Login should be successful"
    assert "message" in response_json and "User exists" in response_json["message"]

def test_verify_login_missing_email():
    """
    Test to verify that the POST /verifyLogin API returns an error
    when the email field is missing from the request payload.
    """

    payload = {
        # "email" is intentionally omitted
        "password": "123"
    }

    response = requests.post(f"{BASE_URL}/verifyLogin", data=payload)

    # Expecting a 200 status with error in body (per API behavior)
    assert response.status_code == 200, "Expected status code 200 even for invalid login"

    response_json = response.json()

    # Expect failure response
    assert response_json.get("responseCode") != 200, "API should not succeed without email"
    assert "message" in response_json
