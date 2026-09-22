from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from ui.web_element import WebElement


class HoversPage(BasePage):
    def __init__(self, page: Page):
        self.actions = PageActions(page)

        super().__init__(page)
        self.users = MultiWebElement(
            locator=page.locator(".figure"),
            description="user figures",
            page=page,
        )

    def hover_user(self, index: int):
        user = self.users.nth(index)
        avatar = WebElement(
            locator=user.locator.locator("img"),
            description=f"Avatar {index}",
            page=self.page,
        )
        avatar.hover()

    def get_username(self, index: int):
        user = self.users.nth(index)
        username = WebElement(
            locator=user.locator.locator(".figcaption h5"),
            description=f"Username {index}",
            page=self.page,
        )
        return username.get_inner_text().strip()
