from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.page_actions import PageActions
from ui.web_element import WebElement


class NewWindowPage(BasePage):
    URL = "https://the-internet.herokuapp.com/windows"

    def __init__(self, page: Page):
        super().__init__(page)
        self.actions = PageActions(page)
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

    def open(self):
        self.page.goto(self.URL)

    def click_here(self):
        return self.click_here_link.click()

    def expect_new_page(self):
        return self.actions.expect_new_page()

    def focus_on_new_window(self):
        return self.actions.bring_to_front()

    def get_new_window_text(self):
        return self.actions.get_text(self.new_window_text)

    def close_window(self):
        self.actions.close_page()

    def get_page_count(self):
        return len(self.page.context.pages)

    def switch_to_first_tab(self):
        pages = self.page.context.pages
        if len(pages) > 0:
            self.pages = pages[0]
            self.page.bring_to_front()
