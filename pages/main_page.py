from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.search_bar = WebElement(
            locator=page.locator("search-input"),
            description="Search Bar",
            page=page,
        )

        self.search_button = WebElement(
            locator=page.locator("search-button"),
            description="Search Button",
            page=page,
        )

    def click_search_bar(self):
        self.search_bar.click()

    def fill_search_bar(self, name):
        self.search_bar.fill(name)

    def click_search_button(self):
        self.search_button.click()
