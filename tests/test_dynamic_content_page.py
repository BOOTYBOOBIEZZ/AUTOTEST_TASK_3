from pages.dynamic_content_page import DynamicContentPage


class TestDynamicContentPage:
    def test_duplicate_images(self, dynamic_content_page: DynamicContentPage):

        dynamic_content_page.get_img_srcs()
        dynamic_content_page.find_same_images()
        dynamic_content_page.has_duplicate_images()
        dynamic_content_page.refresh_until_duplicates()
        duplicates_found = dynamic_content_page.has_duplicate_images() == True

        assert duplicates_found, "Expected duplicates_found is True, but got False!"
