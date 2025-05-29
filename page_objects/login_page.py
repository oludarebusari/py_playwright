import allure
from playwright.sync_api import Page

from page_objects.base_page import BasePage
from page_objects.main_page import MainPage
from helper.utils import log_message, LogLevel, take_screenshot


class LoginPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.username_field = self.page.locator("#user-name")
        self.password_field = self.page.locator("#password")
        self.login_button = self.page.locator("#login-button")

    @allure.step("Performing login with username: {username}")
    def perform_login(self, username: str, password: str) ->MainPage | None:
        """
        Perform login with given credentials.

        Args:
            username (str): Username for login.
            password (str): Password for login.

        Returns:
            MainPage: If login succeeds.
            None: If login fails  
        
        """
        
        log_message(self.logger, "Attempting to log in", level=LogLevel.INFO)
        
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)
        
        if self.login_button.is_visible():
            log_message(self.logger, "Login failed", level=LogLevel.ERROR)
            take_screenshot(self.page, "login_failed")
            return None

        return MainPage(self.page) 