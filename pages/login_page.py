from playwright.sync_api import Page

from pages.base_page import BasePage

from ui.web_element import WebElement


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.success_message = WebElement(
            locator=page.locator("div.example p"),
            description="Success message",
            page=page,
        )

    def get_success_message(self):
        return self.success_message.get_inner_text().strip()
