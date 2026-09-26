from pages.download_page import DownloadPage


class TestDownloadPage:
    def test_download_page(self, download_page: DownloadPage):

        expected_filename = download_page.get_filename_by_index(2)
        download = download_page.download_file_by_index(2)

        assert download.suggested_filename == expected_filename, (
            f"Expected '{expected_filename}', got '{download.suggested_filename}'"
        )
        assert download.failure() is None, "Download failed"
