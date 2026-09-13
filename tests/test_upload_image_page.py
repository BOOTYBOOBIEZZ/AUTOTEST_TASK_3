from playwright.sync_api import Page

from pages.upload_image_page import UploadPage
from ui.page_actions import PageActions


class TestUploadPage:
    def test_upload_file(self, page: Page):

        upload_page = UploadPage(page)
        self.actions = PageActions(page)

        upload_page.open()
        file_path = "C:/WORK/pics/200x200.png"

        upload_page.upload_file(file_path)

        upload_page.expect_uploaded_page()

        uploaded_text = upload_page.get_upload_text()
        assert uploaded_text == "File Uploaded!", (
            f"Expected 'File Uploaded!', got '{uploaded_text}'"
        )
