from playwright.sync_api import Page

from ui.page_actions import PageActions


class BasePage:
    def __init__(self, page: Page):
        self.actions = PageActions(page)
        self.page = page

    def open(self, url: str):
        self.actions.goto(url)
