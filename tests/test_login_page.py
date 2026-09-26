from pages.login_page import LoginPage


class TestLoginPage:
    def test_login(self, login_page: LoginPage):
        success_message = login_page.get_success_message()
        expected_message = "Congratulations! You must have the proper credentials."
        actual_message = success_message.strip()
        assert actual_message == expected_message, (
            f"Expected '{expected_message}', but got '{actual_message}'"
        )
