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

    @allure.step("login")
    def perform_login(self, username: str, password: str) ->MainPage:
        log_message(self.logger,"performing login",level=LogLevel.INFO)
        self.type_text(self.username_field, username)
        self.type_text(self.password_field, password)
        self.click_element(self.login_button)
        if self.login_button.is_visible():
            log_message(self.logger, "Login failed", level=LogLevel.ERROR)
            take_screenshot(self.page, "login_failed")
            return None

        return MainPage(self.page) 