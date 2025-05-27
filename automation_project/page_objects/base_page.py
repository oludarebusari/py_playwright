from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page
    
    def safe_execute(self, action, action_name: str, *args):
        """Executes an action safely, catching exceptions."""
        try:
            return 
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
        
    def click_element(self, locator):
        """Clicks an element on the page."""
        self.safe_execute(self.page.click, "click_element", locator)