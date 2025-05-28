from venv import logger

import pytest
import sys
import os

# Add the parent directories of 'helper' and 'page_objects' to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from page_objects.login_page import LoginPage
from page_objects.main_page import MainPage
from helper.config import BASE_URL
from helper.utils import log_message, LogLevel
from helper.validation import AppValidation


@pytest.fixture()
def setup_playwright(playwright, request):
    headed = request.config.getoption("--headed", default=False)
    browser = playwright.chromium.launch(headless=not headed)
    page = browser.new_page()
    try:
        yield page
    finally:
        log_message(logger,"closing browser", LogLevel.INFO)
        browser.close()

@pytest.fixture()
def setup_login_page(setup_playwright):
    login_page = LoginPage(setup_playwright)
    login_page.navigate_to(BASE_URL)
    log_message(logger, "navigate to login page")
    yield login_page

@pytest.fixture()
def setup_all_pages(setup_playwright):
    login_page = LoginPage(setup_playwright)
    main_page = MainPage(setup_playwright)
    yield login_page, main_page

@pytest.fixture()
def validation(setup_all_pages):
    yield AppValidation(setup_all_pages)