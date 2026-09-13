from playwright.sync_api import Page

from pages.base_page import BasePage
from pages.login_page import LoginPage


class TestLoginPage:
    def test_LoginPage(self, page: Page):
        base_page = BasePage(page)

        login_page = base_page.get_page(LoginPage)
        login_page.open()
        success_message = login_page.get_success_message()
        expected_message = "Congratulations! You must have the proper credentials."
        actual_message = success_message.strip()
        assert actual_message == expected_message, (
            f"Expected '{expected_message}', but got '{actual_message}'"
        )
