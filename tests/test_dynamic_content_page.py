from playwright.sync_api import Page

from pages.dynamic_content_page import DynamicContentPage
from utils.url_utils import DYNAMIC_CONTENT_URL


class TestDynamicContentPage:
    def test_duplicate_images(self, page: Page):

        dynamic_page = DynamicContentPage(page)

        dynamic_page.open(DYNAMIC_CONTENT_URL)

        dynamic_page.get_img_srcs()
        dynamic_page.find_same_images()
        dynamic_page.has_duplicate_images()
        dynamic_page.refresh_until_duplicates()
        duplicates_found = dynamic_page.has_duplicate_images() == True

        assert duplicates_found, "Expected duplicates_found is True, but got False!"
