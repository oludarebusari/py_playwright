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
from playwright.sync_api import Playwright, Page, Browser


@pytest.fixture()
def setup_playwright(playwright: Playwright, request) -> Page: 
    # Determine if browser should run in headed mode
    headed: bool = request.config.getoption("--headed") or False

    # Launch the Chromium browser
    browser: Browser = playwright.chromium.launch(headless=not headed)
    
    # Create a new page (tab) in the browser
    page: Page = browser.new_page()
    
    # Provide the page to the test
    yield page

    # Cleanup: log and close the browser after the test
    log_message(logger, "Closing the browser", LogLevel.INFO)
    browser.close()


@pytest.fixture
def setup_login_page(setup_playwright):
    # setup_playwright gives you a Playwright Page
    page = setup_playwright

    # Initialize the LoginPage object using the page
    login_page = LoginPage(page)
    
    # Navigate to the login page
    login_page.navigate_to(BASE_URL)
    log_message(logger, "Navigated to login page")

    # Provide the login page to the test
    yield login_page


@pytest.fixture
def setup_all_pages(setup_playwright):
    page = setup_playwright

    # Initialize page objects
    login_page = LoginPage(page)
    main_page = MainPage(page)

    # Optionally, navigate to the starting page (like login)
    login_page.navigate_to(BASE_URL)
    log_message(logger, "Navigated to login page")

    # Yield both page objects to the test
    yield login_page, main_page


@pytest.fixture()
def validation(setup_all_pages):
    yield AppValidation(setup_all_pages)