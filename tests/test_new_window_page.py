from playwright.sync_api import Page

from pages.new_window_page import NewWindowPage
from pages.new_window_result_page import NewWindowResultPage
from utils.browser_manager import BrowserManager


class TestNewWindow:
    def test_new_window(self, new_window_page: NewWindowPage, page: Page):
        browser_manager = BrowserManager(page.context)

        first_tab = page

        with page.context.expect_page() as new_page_info:
            new_window_page.click_here()
        new_page_1 = new_page_info.value
        new_page_1.wait_for_load_state()

        result_page_1 = NewWindowResultPage(new_page_1)
        expected_result_1 = "New Window"
        actual_result_1 = result_page_1.get_result_text()
        assert actual_result_1 == expected_result_1, (
            f"Expected {expected_result_1}, but got {actual_result_1}"
        )

        first_tab.bring_to_front()

        with page.context.expect_page() as new_page_info:
            new_window_page.click_here()
        new_page_2 = new_page_info.value
        new_page_2.wait_for_load_state()

        result_page_2 = NewWindowResultPage(new_page_2)

        expected_result_2 = "New Window"
        actual_result_2 = result_page_2.get_result_text()
        assert actual_result_2 == expected_result_2, (
            f"Expected {expected_result_2}, but got {actual_result_2}"
        )

        first_tab.bring_to_front()

        new_page_1.close()

        new_page_2.close()

        expected_pages = 1
        actual_pages = browser_manager.get_page_count()
        assert expected_pages == actual_pages, (
            f"Expected {expected_pages} page, got {actual_pages}"
        )
