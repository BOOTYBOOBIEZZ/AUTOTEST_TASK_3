from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class NewWindowPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.click_here_link = WebElement(
            locator=page.locator("a:has-text('Click Here')"),
            description="Ссылка 'Click here'",
            page=page,
        )
        self.new_window_text = WebElement(
            locator=page.locator("h3:has-text('New Window')"),
            description="Текст 'new window'",
            page=page,
        )

    def click_here(self):
        return self.click_here_link.click()
