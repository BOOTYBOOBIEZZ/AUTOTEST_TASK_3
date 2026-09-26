from pages.scroll_page import ScrollPage


class TestScrollPage:
    def test_scroll_to_10_paragraphs(self, scroll_page: ScrollPage):

        final_count = scroll_page.scroll_until_paragraphs_count(
            target_count=10, max_scrolls=30
        )

        assert final_count >= 10, (
            f"Expected at least 10 paragraphs, but got {final_count}"
        )
