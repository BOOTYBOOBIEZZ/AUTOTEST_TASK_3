from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class DownloadPage(BasePage):
    def __init__(self, page: Page):
        self.actions = PageActions(page)

        self.files = MultiWebElement(
            locator=page.locator(".example a"),
            description="all file for download",
            page=page,
        )

    def get_filename_by_index(self, index: int):
        return self.files.nth(index).get_inner_text()

    def download_file_by_index(self, index: int):
        with self.page.expect_download() as download_info:
            self.files.nth(index).click()
        return download_info.value
