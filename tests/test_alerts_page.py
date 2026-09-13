import pytest
from playwright.sync_api import Page

from pages.alerts_page import AlertsPage


class TestAlertsPage:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        """Создаёт и открывает страницу алертов перед каждым тестом."""
        self.alerts_page = AlertsPage(page)
        self.alerts_page.open()

    def test_js_alert(self):
        self.alerts_page.open()

        dialog_message = self.alerts_page.click_js_alert_button()
        assert dialog_message == "I am a JS Alert", (
            f"Expected alert message 'I am a JS Alert', but got '{dialog_message}'"
        )
        result_text = self.alerts_page.get_result_text()
        expected_text = "You successfully clicked an alert"
        assert result_text == expected_text, (
            f"Expected '{expected_text}', but got '{result_text}'"
        )

    def test_js_confirm_ok(self):
        self.alerts_page.open()

        dialog_message = self.alerts_page.click_js_confirm_and_accept()
        assert dialog_message == "I am a JS Confirm"

        result_text = self.alerts_page.get_result_text()
        assert result_text == "You clicked: Ok"

    def test_js_confirm_cancel(self):
        self.alerts_page.open()

        dialog_message = self.alerts_page.click_js_confirm_and_dismiss()
        assert dialog_message == "I am a JS Confirm"

        result_text = self.alerts_page.get_result_text()
        assert result_text == "You clicked: Cancel"

    def test_js_prompt(self):
        self.alerts_page.open()
        random_text = self.alerts_page.generate_random_text()
        dialog_message = self.alerts_page.click_js_prompt_button(random_text)
        assert dialog_message == "I am a JS prompt", (
            f"Expected alert message 'I am a JS prompt', but got '{dialog_message}'"
        )
        result_text = self.alerts_page.get_result_text()
        expected_text = f"You entered: {random_text}"
        assert result_text == expected_text, (
            f"Expected '{expected_text}', but got '{result_text}'"
        )
