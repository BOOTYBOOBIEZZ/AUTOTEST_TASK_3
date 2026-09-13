from playwright.sync_api import Page

from pages.horizontal_slider_page import HorizontalSliderPage


class TestHorizontalSliderPage:
    def test_slider_via_keyboard(self, page: Page):
        slider_page = HorizontalSliderPage(page)
        slider_page.open()

        steps = slider_page.generate_random_steps()
        expected_value = float(steps * 0.5)

        slider_page.set_slider_value_via_keyboard(steps)

        actual_value = slider_page.get_slider_value()

        assert actual_value == expected_value, (
            f"Expected '{expected_value}', but got '{actual_value}'"
        )
