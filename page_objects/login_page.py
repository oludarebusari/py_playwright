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
        self.error_message = self.page.locator("[data-test='error']")  
        

    @allure.step("Performing login with username: {username}")
    def perform_login(self, username: str, password: str) -> MainPage:
        """
            Attempt login and return MainPage if successful, else return None.
    
        """
        log_message(self.logger, "Attempting to log in", level=LogLevel.INFO)

        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)

        # Wait for possible error message or page transition
        if self.error_message.is_visible(timeout=3000):
            log_message(self.logger, "Login failed", level=LogLevel.ERROR)
            take_screenshot(self.page, "login_failed")
            return None

        return MainPage(self.page)


    def get_error_message(self) -> str:
        """
            Get the error message displayed on the login page.
        """
        if self.error_message.is_visible():
            error_text = self.error_message.inner_text()
            log_message(self.logger, f"Error message displayed: {error_text}", level=LogLevel.ERROR)
            take_screenshot(self.page, "login_failed")
            return error_text
        else:
            log_message(self.logger, "No error message displayed", level=LogLevel.INFO)
            return ""   