import random

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class HorizontalSliderPage(BasePage):
    URL = "https://the-internet.herokuapp.com/horizontal_slider"

    def __init__(self, page: Page):
        super().__init__(page)
        self.slider = WebElement(
            locator=page.get_by_role("slider"),
            description="Горизонтальный слайдер",
            page=page,
        )

        self.slider_value = WebElement(
            locator=page.locator("#range"),
            description="Значение слайдера",
            page=page,
        )

    def open(self):
        self.page.goto(self.URL)

    def set_slider_value_via_keyboard(self, steps: int):
        self.slider.focus()
        for _ in range(steps):
            self.slider.press("ArrowRight")

    def get_slider_value(self):
        return self.slider_value.get_text_content().strip()

    def generate_random_steps(self):
        return random.randint(1, 10)

    def generate_random_value(self):
        steps = random.randint(1, 10)
        return steps * 0.5
