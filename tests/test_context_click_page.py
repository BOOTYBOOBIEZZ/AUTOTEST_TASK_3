from pages.context_click_page import ContextClickPage


class TestContextClickPage:
    def test_context_box(self, context_click_page: ContextClickPage):

        alert_text = context_click_page.right_click_hot_spot()

        expected_text = "You selected a context menu"
        assert alert_text == expected_text, (
            f"Expected text '{expected_text}', but got {alert_text}"
        )
