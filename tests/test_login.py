import pytest

import sys
import os

# Add the parent directories of 'helper' and 'page_objects' to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from helper.config import VALID_CREDENTIALS
from helper.validation import AppValidation


def test_successfully_login(setup_login_page,validation):
    login_page = setup_login_page
    main_page = login_page.perform_login(VALID_CREDENTIALS["email"],VALID_CREDENTIALS["password"])
    assert main_page is not None, "Login failed unexpectedly!"

    validation.validate_logged_in()



@pytest.mark.parametrize(
    "email, password, expected_error",
    [
        ("test_username","secret_sauce","Epic sadface: Username and password do not match any user in this service"),
        ("standard_user","wrong_password","Epic sadface: Username and password do not match any user in this service"),

    ],
    ids=[
        "Invalid username with valid password",
        "Valid username with invalid password"
    ]
)
def test_invalid_login_and_verify_error_message(setup_login_page,validation,email, password, expected_error):
    login_page = setup_login_page
    main_page = login_page.perform_login(email, password)

    actual_error = login_page.get_error_message()
    validation.validate_failed_login(actual_error, expected_error)