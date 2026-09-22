from playwright.sync_api import Page

from pages.context_click_page import ContextClickPage
from utils.url_utils import CONTEXT_MENU_URL


class TestContextClickPage:
    def test_context_box(self, page: Page):
        context_page = ContextClickPage(page)

        context_page.open(CONTEXT_MENU_URL)

        alert_text = context_page.right_click_hot_spot()

        expected_text = "You selected a context menu"
        assert alert_text == expected_text, (
            f"Expected text '{expected_text}', but got {alert_text}"
        )
