from enum import StrEnum

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class Users(StrEnum):
    USER_1 = "user1"
    USER_2 = "user2"
    USER_3 = "user3"


class HoversPage(BasePage):
    URL = "https://the-internet.herokuapp.com/hovers"

    def __init__(self, page: Page):
        super().__init__(page)
        self.user_1 = WebElement(
            locator=page.get_by_text("name: user1"),
            description="User 1",
            page=page,
        )

        self.user_2 = WebElement(
            locator=page.get_by_text("name: user2"),
            description="User 2",
            page=page,
        )

        self.user_3 = WebElement(
            locator=page.get_by_text("name: user3"),
            description="User 3",
            page=page,
        )

        self.avatar_1 = WebElement(
            locator=page.locator(".figure").nth(0).locator("img"),
            description="Аватар 1",
            page=page,
        )
        self.avatar_2 = WebElement(
            locator=page.locator(".figure").nth(1).locator("img"),
            description="Аватар 2",
            page=page,
        )
        self.avatar_3 = WebElement(
            locator=page.locator(".figure").nth(2).locator("img"),
            description="Аватар 3",
            page=page,
        )

    def open(self):
        self.actions.goto(self.URL)

    def hover_on_image(self, avatar: WebElement):
        avatar.hover()

    def get_user_name(self, user_element: WebElement):
        return user_element.get_inner_text()
