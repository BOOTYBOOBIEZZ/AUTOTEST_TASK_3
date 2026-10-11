from pages.dynamic_content_page import DynamicContentPage


class TestDynamicContentPage:
    def test_duplicate_images(self, dynamic_content_page: DynamicContentPage):
        dynamic_content_page.refresh_until_duplicates(max_attempts=10)
        duplicates_found = dynamic_content_page.has_duplicate_images()

        assert duplicates_found, "Expected duplicates_found is True, but got False!"
