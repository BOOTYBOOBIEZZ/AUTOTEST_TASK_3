from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    URL = "https://the-internet.herokuapp.com/basic_auth"

    def __init__(self, page: Page):
        super().__init__(page)
        self.success_message = self.page.locator("div.example p")

    def open(self):
        self.page.goto(self.URL)

    def get_success_message(self):
        return self.success_message.inner_text().strip()
