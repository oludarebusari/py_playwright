from playwright.sync_api import expect

from page_objects.base_page import BasePage
from helper.utils import take_screenshot, log_message, LogLevel


class AppValidation(BasePage):
    def __init__(self, setup_all_pages):
        self.login_page, self.main_page = setup_all_pages
        super().__init__(self.login_page)


    def validate_logged_in(self):
        login_button = self.login_page.login_button
        try:
            expect(login_button).to_be_hidden()
        except:
            log_message(self.logger,"login failed", LogLevel.ERROR)
            take_screenshot("login failed")
            raise "Login failed"


    def validate_failed_login(self, actual_error: str, expected_error: str):
        assert actual_error == expected_error, f"Expected error message '{expected_error}', but got '{actual_error}'"
        log_message(self.logger, f"Expected error message '{expected_error}' matches actual error '{actual_error}'", LogLevel.INFO)
