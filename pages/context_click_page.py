from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.page_actions import PageActions
from ui.web_element import WebElement


class ContextClickPage(BasePage):
    def __init__(self, page: Page):
        self.actions = PageActions(page)

        self.hot_spot = WebElement(
            locator=page.locator("#hot-spot"),
            description="Контекстное меню (hot-spot)",
            page=page,
        )

    def right_click_hot_spot(self):
        return self.actions.run_and_accept_alert(
            action=lambda: self.hot_spot.right_click()
        )
