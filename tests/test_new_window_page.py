from playwright.sync_api import Page

from pages.new_window_page import NewWindowPage
from pages.new_window_result_page import NewWindowResultPage
from utils.browser_manager import BrowserManager
from utils.url_utils import NEW_WINDOW_URL


class TestNewWindow:
    def test_new_window(self, page: Page):
        new_window_page = NewWindowPage(page)
        browser_manager = BrowserManager(page.context)

        new_window_page.open(NEW_WINDOW_URL)

        first_tab = page

        with page.context.expect_page() as new_page_info:
            new_window_page.click_here()
        new_page_1 = new_page_info.value
        new_page_1.wait_for_load_state()

        result_page_1 = NewWindowResultPage(new_page_1)
        assert result_page_1.get_result_text() == "New Window"

        first_tab.bring_to_front()

        with page.context.expect_page() as new_page_info:
            new_window_page.click_here()
        new_page_2 = new_page_info.value
        new_page_2.wait_for_load_state()

        result_page_2 = NewWindowResultPage(new_page_2)

        assert result_page_2.get_result_text() == "New Window"

        first_tab.bring_to_front()

        new_page_1.close()

        new_page_2.close()

        assert browser_manager.get_page_count() == 1, (
            "Expected 1 page, got {browser_manager.get_page_count()}"
        )
