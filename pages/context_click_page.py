from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class ContextClickPage(BasePage):
    URL = "https://the-internet.herokuapp.com/context_menu"

    def __init__(self, page: Page):
        super().__init__(page)
        self.hot_spot = WebElement(
            locator=page.locator("#hot-spot"),
            description="Контекстное меню (hot-spot)",
            page=page,
        )

    def open(self):
        self.page.goto(self.URL)

    def right_click_hot_spot(self):
        return self.actions.run_and_accept_alert(
            action=lambda: self.hot_spot.right_click()
        )
