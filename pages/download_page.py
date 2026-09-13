from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement
from ui.page_actions import PageActions


class DownloadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/download"

    def __init__(self, page: Page):
        super().__init__(page)
        self.actions = PageActions(page)

        self.all_files = MultiWebElement(
            locator=page.locator(".example a"),
            description="all file for download",
            page=page,
        )

        self.txt_files = MultiWebElement(
            locator=page.locator(".example a[href$='.txt']"),
            description=".txt файлы",
            page=page,
        )

        self.png_files = MultiWebElement(
            locator=page.locator(".example a[href$='.png']"),
            description=".png файлы",
            page=page,
        )

        self.pdf_files = MultiWebElement(
            locator=page.locator(".example a[href$='.pdf']"),
            description=".pdf файлы",
            page=page,
        )

        # ✅ Все ссылки на файлы с расширением .jpg или .jpeg
        self.jpg_files = MultiWebElement(
            locator=page.locator(".example a[href$='.jpg'], .example a[href$='.jpeg']"),
            description=".jpg/.jpeg файлы",
            page=page,
        )

    def open(self):
        self.actions.goto(self.URL)

    def get_filename_by_index(self, index: int):
        return [self.all_files.nth(index).get_inner_text()]

    def download_file_by_index(self, index: int):
        self.all_files.nth(index).click()
