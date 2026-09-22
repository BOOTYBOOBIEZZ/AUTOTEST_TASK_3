from playwright.sync_api import Page

from pages.login_page import LoginPage
from utils.url_utils import LOGIN_URL


class TestLoginPage:
    def test_login(self, page: Page):
        login_page = LoginPage(page)

        login_page.open(LOGIN_URL)

        success_message = login_page.get_success_message()
        expected_message = "Congratulations! You must have the proper credentials."
        actual_message = success_message.strip()
        assert actual_message == expected_message, (
            f"Expected '{expected_message}', but got '{actual_message}'"
        )
