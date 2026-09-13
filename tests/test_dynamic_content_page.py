from playwright.sync_api import Page

from pages.dynamic_content_page import DynamicContentPage
from ui.page_actions import PageActions


class TestDynamicContentPage:
    def test_duplicate_images(self, page: Page):

        dynamic_page = DynamicContentPage(page)
        self.actions = PageActions(page)

        dynamic_page.open()

        dynamic_page.get_img_srcs()
        dynamic_page.find_same_images()
        dynamic_page.has_duplicate_images()
        dynamic_page.refresh_until_duplicates()
        duplicates_found = dynamic_page.has_duplicate_images() == True

        assert duplicates_found == True, (
            "Expected duplicates_found is True, but got False!"
        )
