import logging

from playwright.sync_api import Page, expect

from logger import LOGGER_NAME
from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement
from ui.web_element import WebElement

logger = logging.getLogger(LOGGER_NAME)


class ScrollPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.scroll_container = WebElement(
            locator=page.locator("#page"),
            description="Page container",
            page=page,
        )

        self.paragraphs = MultiWebElement(
            locator=page.locator(".jscroll-added"),
            description="paragraphs",
            page=page,
        )

        self.last_paragraph = WebElement(
            locator=page.locator(".jscroll-added").last,
            description="Last paragraph",
            page=page,
        )

    def count_paragraphs(self):
        return self.paragraphs.count()

    def scroll_to_bottom(self):
        self.last_paragraph.scroll_into_view_if_needed()

    def wait_for_more_paragraphs(self, current_count: int, timeout: int = 5000) -> None:
        self.paragraphs.nth(current_count).locator.wait_for(
            state="attached", timeout=timeout
        )

    def scroll_until_paragraphs_count(
        self,
        target_count: int = 10,
        max_scrolls: int = 30,
    ) -> int:
        for attempt in range(max_scrolls):
            current_count = self.count_paragraphs()

            if current_count >= target_count:
                logger.info(
                    f"Target reached: {target_count} paragraphs after {attempt} scrolls"
                )
                return current_count

            logger.info(
                f"Scroll {attempt + 1}: {current_count}/{target_count} paragraphs"
            )

            self.scroll_to_bottom()

            self.wait_for_more_paragraphs(current_count)

        final_count = self.count_paragraphs()
        logger.info(f"Max scrolls reached. Final count: {final_count} paragraphs")
        return final_count
