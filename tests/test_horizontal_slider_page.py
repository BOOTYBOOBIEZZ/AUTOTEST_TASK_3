from playwright.sync_api import Page

from pages.horizontal_slider_page import HorizontalSliderPage
from utils.url_utils import HORIZONTAL_URL


class TestHorizontalSliderPage:
    def test_slider_via_keyboard(self, page: Page):
        slider_page = HorizontalSliderPage(page)

        slider_page.open(HORIZONTAL_URL)

        steps = slider_page.generate_random_steps()
        expected_value = steps * slider_page._get_slider_step()

        slider_page.set_slider_value_via_keyboard(steps)

        actual_value = float(slider_page.get_slider_value())
        assert actual_value == expected_value, (
            f"Expected {expected_value}, got {actual_value}"
        )

    def test_slider_random_value(self, page: Page):
        slider_page = HorizontalSliderPage(page)

        slider_page.open(HORIZONTAL_URL)

        random_value = slider_page.generate_random_value()
        slider_page.set_slider_to_value(random_value)

        actual_value = float(slider_page.get_slider_value())

        assert actual_value == random_value, (
            f"Expected {random_value}, but got {actual_value}"
        )
