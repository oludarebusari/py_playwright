BASE_URL = "https://saucedemo.com"

VALID_CREDENTIALS = {
    "email": "standard_user",
    "password": "secret_sauce"
}
INVALID_CREDENTIALS_WITHOUT_PASSWORD = {
    "email": "standard_user",
    "password": ""
}

INVALID_CREDENTIALS = {
    "email": "invalid_user",
    "password": "invalid_password"
}

INVALID_CREDENTIALS_WITH_WRONG_PASSWORD = {
    "email": "standard_user",
    "password": "wrong_password"
}

INVALID_CREDENTIALS_WITH_WRONG_EMAIL = {
    "email": "wrong_user",
    "password": "secret_sauce"
}

INVALID_CREDENTIALS_WITH_WRONG_EMAIL_AND_PASSWORD = {
    "email": "wrong_user",
    "password": "wrong_password"
}

INVALID_CREDENTIALS_WITH_WRONG_EMAIL_AND_PASSWORD_2 = {
    "email": "wrong_user_2",
    "password": "wrong_password_2"
}

