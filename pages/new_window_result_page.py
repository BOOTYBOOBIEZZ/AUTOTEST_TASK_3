from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class NewWindowResultPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.heading = WebElement(
            locator=page.locator("h3"), description="New Window Result Head", page=page
        )

    def get_result_text(self):
        return self.heading.get_inner_text().strip()
