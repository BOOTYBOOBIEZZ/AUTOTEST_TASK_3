from pages.upload_image_page import UploadPage


class TestUploadPage:
    def test_upload_file(self, upload_image_page: UploadPage):

        file_path = "C:/WORK/pics/200x200.png"

        upload_image_page.upload_file(file_path)

        uploaded_text = upload_image_page.get_upload_text()
        assert uploaded_text == "File Uploaded!", (
            f"Expected 'File Uploaded!', got '{uploaded_text}'"
        )
