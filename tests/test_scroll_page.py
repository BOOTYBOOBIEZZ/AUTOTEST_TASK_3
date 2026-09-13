from playwright.sync_api import Page

from pages.scroll_page import ScrollPage
from ui.page_actions import PageActions


class TestScrollPage:
    def test_scroll_to_10_paragraphs(self, page: Page):

        scroll_page = ScrollPage(page)
        self.actions = PageActions(page)

        scroll_page.open()

        final_count = scroll_page.scroll_until_paragraphs_count(
            target_count=10, max_scrolls=30, wait_after_scroll=500
        )

        assert final_count >= 10, (
            f"Expected at least 10 paragraphs, but got {final_count}"
        )
