import random

from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.page_actions import PageActions
from ui.web_element import WebElement


class HorizontalSliderPage(BasePage):
    def __init__(self, page: Page):
        self.actions = PageActions(page)

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

    def _get_slider_min(self):
        min_val = self.slider.get_attribute("min")
        return float(min_val)

    def _get_slider_max(self):
        max_val = self.slider.get_attribute("max")
        return float(max_val)

    def _get_slider_step(self):
        step_val = self.slider.get_attribute("step")
        return float(step_val)

    def set_slider_value_via_keyboard(self, steps: int):
        self.slider.focus()
        for _ in range(steps):
            self.slider.press("ArrowRight")

    def set_slider_to_value(self, target_value: float) -> None:
        self.slider.locator.evaluate(f"(element) => element.value = '{target_value}'")
        self.slider.locator.evaluate(
            "(element) => element.dispatchEvent(new Event('change'))"
        )

    def get_slider_value(self):
        return self.slider_value.get_text_content().strip()

    def generate_random_steps(self):
        min_val = self._get_slider_min()
        max_val = self._get_slider_max()
        step = self._get_slider_step()

        max_steps = int((max_val - min_val) / step)
        return random.randint(1, max_steps)

    def generate_random_value(self):

        min_val = self._get_slider_min()
        max_val = self._get_slider_max()
        step = self._get_slider_step()

        max_steps = int((max_val - min_val) / step)
        random_steps = random.randint(0, max_steps)

        return min_val + (random_steps * step)
