import pytest
from playwright.sync_api import Page

from pages.alerts_page import AlertsPage
from utils.random import RandomText
from utils.url_utils import ALERTS_URL


class TestAlertsPage:
    @pytest.fixture(autouse=True)
    def setup(self, page: Page):
        self.alerts_page = AlertsPage(page)
        self.alerts_page.open(ALERTS_URL)

    def test_js_alert(self):

        dialog_message = self.alerts_page.click_js_alert_button()
        expected_message = "I am a JS Alert"
        assert dialog_message == expected_message, (
            f"Expected '{expected_message}', but got '{dialog_message}'"
        )
        result_text = self.alerts_page.get_result_text()
        expected_text = "You successfully clicked an alert"
        assert result_text == expected_text, (
            f"Expected '{expected_text}', but got '{result_text}'"
        )

    def test_js_confirm_ok(self):

        dialog_message = self.alerts_page.click_js_confirm_and_accept()
        expected_message = "I am a JS Confirm"

        assert dialog_message == expected_message, (
            f"Expected '{expected_message}', but got '{dialog_message}'"
        )
        result_text = self.alerts_page.get_result_text()
        assert result_text == "You clicked: Ok"

    def test_js_confirm_cancel(self):

        dialog_message = self.alerts_page.click_js_confirm_and_dismiss()
        expected_message = "I am a JS Confirm"
        assert dialog_message == expected_message, (
            f"Expected '{expected_message}', but got '{dialog_message}'"
        )

        result_text = self.alerts_page.get_result_text()
        assert result_text == "You clicked: Cancel"

    def test_js_prompt(self):

        random_text = RandomText()
        gen_random_text = random_text.generate_random_text()
        dialog_message = self.alerts_page.click_js_prompt_button(gen_random_text)
        expected_message = "I am a JS prompt"

        assert dialog_message == expected_message, (
            f"Expected '{expected_message}', but got '{dialog_message}'"
        )

        result_text = self.alerts_page.get_result_text()
        expected_text = f"You entered: {gen_random_text}"
        assert result_text == expected_text, (
            f"Expected '{expected_text}', but got '{result_text}'"
        )
