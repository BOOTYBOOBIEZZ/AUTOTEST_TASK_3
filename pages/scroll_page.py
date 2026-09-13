from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions
from ui.web_element import WebElement


class ScrollPage(BasePage):
    URL = "https://the-internet.herokuapp.com/infinite_scroll"

    def __init__(self, page: Page):
        super().__init__(page)

        self.actions = PageActions(page)

        self.scroll_container = WebElement(
            locator=page.locator("#page"),
            description="Контейнер страницы",
            page=page,
        )

        self.paragraphs = MultiWebElement(
            locator=page.locator(".jscroll-added"),
            description="paragraphs",
            page=page,
        )

        self.last_paragraph = WebElement(
            locator=page.locator(".jscroll-added").last,
            description="Последний параграф",
            page=page,
        )

    def open(self):
        self.actions.goto(self.URL)

    def count_paragraphs(self):
        return self.paragraphs.count()

    def scroll_to_bottom(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_until_paragraphs_count(
        self,
        target_count: int = 10,
        max_scrolls: int = 30,
        wait_after_scroll: int = 500,
    ) -> int:
        for attempt in range(max_scrolls):
            current_count = self.count_paragraphs()

            if current_count >= target_count:
                print(
                    f"Target reached: {target_count} paragraphs after {attempt} scrolls"
                )
                return current_count

            self.scroll_to_bottom()

            self.page.wait_for_timeout(wait_after_scroll)

        final_count = self.count_paragraphs()
        print(f"Max scrolls reached. Final count: {final_count} paragraphs")
        return final_count
