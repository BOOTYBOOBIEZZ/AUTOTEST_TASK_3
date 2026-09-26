from pages.horizontal_slider_page import HorizontalSliderPage


class TestHorizontalSliderPage:
    def test_slider_random_value(self, horizontal_slider_page: HorizontalSliderPage):

        random_value = horizontal_slider_page.generate_random_value()
        horizontal_slider_page.set_slider_to_value(random_value)

        actual_value = float(horizontal_slider_page.get_slider_value())

        assert actual_value == random_value, (
            f"Expected {random_value}, but got {actual_value}"
        )
