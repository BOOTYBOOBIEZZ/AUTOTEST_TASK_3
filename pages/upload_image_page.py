from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.page_actions import PageActions
from ui.web_element import WebElement


class UploadPage(BasePage):
    URL = "https://the-internet.herokuapp.com/upload"

    def __init__(self, page: Page):
        super().__init__(page)

        self.actions = PageActions(page)

        self.choose_file_button = WebElement(
            locator=page.locator("#file-upload"), description="choose_button", page=page
        )

        self.upload_button = WebElement(
            locator=page.locator("#file-submit"),
            description="upload_button",
            page=page,
        )

        self.uploaded_text = WebElement(
            locator=page.locator("h3"),
            description="succesful uploaded text",
            page=page,
        )

        self.uploaded_filename = WebElement(
            locator=page.locator("#uploaded_files"),
            description="Uploaded file",
            page=page,
        )

    def open(self):
        self.actions.goto(self.URL)

    def upload_file(self, file_path: str):
        self.choose_file_button.locator.set_input_files(file_path)
        self.upload_button.click()

    def expect_uploaded_page(self):
        self.actions.expect_new_page()

    def get_upload_text(self):
        return self.uploaded_text.get_inner_text().strip()

    def get_uploaded_filename(self):
        return self.uploaded_filename.get_inner_text().strip()
