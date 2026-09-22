import logging
from typing import Counter

from playwright.sync_api import Page

from logger import LOGGER_NAME
from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions

logger = logging.getLogger(LOGGER_NAME)


class DynamicContentPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.actions = PageActions(page)

        self.images = MultiWebElement(
            locator=page.locator("img[src^='/img/avatars/']"),
            description="images",
            page=page,
        )

    def get_img_srcs(self):
        return [img.get_attribute("src") for img in self.images.all()]

    def get_image_count(self):
        return self.images.count()

    def find_same_images(self) -> set[str]:
        srcs = self.get_img_srcs()
        return {src for src in srcs if srcs.count(src) > 1}

    def has_duplicate_images(self) -> bool:
        return len(self.find_same_images()) > 0

    def refresh_until_duplicates(self, max_attempts: int = 10):
        for attempt in range(max_attempts):
            if self.has_duplicate_images():
                logger.info(f"Duplicates found after {attempt + 1} attempt(s)!")
                return True
            else:
                self.page.reload()
