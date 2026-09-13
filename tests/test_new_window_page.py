from playwright.sync_api import Page

from pages.windows_page import NewWindowPage


class TestNewWindow:
    def test_new_window(self, page: Page):
        new_window_page = NewWindowPage(page)
        new_window_page.open()

        opened_pages = []

        for _ in range(2):
            with new_window_page.expect_new_page() as new_page_info:
                new_window_page.click_here()
            new_page = new_page_info.value

            new_page.bring_to_front()

            assert new_window_page.get_new_window_text() == "Opening a new window"
            opened_pages.append(new_page)

            page.bring_to_front()

        for new_page in opened_pages:
            new_page.close()

        assert len(page.context.pages) == 1, "Должна быть открыта ровно 1 вкладка"
