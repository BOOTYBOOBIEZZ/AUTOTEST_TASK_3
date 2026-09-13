from playwright.sync_api import Page

from pages.download_page import DownloadPage
from ui.page_actions import PageActions


class TestDownloadPage:
    def test_download_page(self, page: Page):
        download_page = DownloadPage(page)
        self.aactions = PageActions(page)

        download_page.open()

        actual_filename = download_page.get_filename_by_index(2)
        print(f"Filename is '{actual_filename}'")

        download_page.download_file_by_index(2)

        page.wait_for_timeout(2000)
