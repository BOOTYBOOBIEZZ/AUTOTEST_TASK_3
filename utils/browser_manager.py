import logging

from playwright.sync_api import BrowserContext, Page

from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class BrowserManager:
    def __init__(self, context: BrowserContext) -> None:
        self.context = context

    def get_pages(self):
        return self.context.pages

    def get_page_count(self):
        return len(self.context.pages)

    def switch_to_page(self, index: int):
        pages = self.get_pages()
        if 0 <= index < len(pages):
            page = pages[index]
            logger.info(f"Switched to page {index}")
            page.bring_to_front()
            return page

        return IndexError(f"Page index {index} out of range")

    def switch_to_first_tab(self):
        return self.switch_to_page(0)

    def close_page(self, page: Page):
        page.close()
        logger.info("Page closed")
