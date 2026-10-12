import logging
import random

from playwright.sync_api import Page

from logger import LOGGER_NAME
from pages.base_page import BasePage
from ui.web_element import WebElement

logger = logging.getLogger(LOGGER_NAME)


class HorizontalSliderPage(BasePage):
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

    def _get_slider_min(self):
        min_val = self.slider.get_attribute("min")
        return float(min_val)

    def _get_slider_max(self):
        max_val = self.slider.get_attribute("max")
        return float(max_val)

    def _get_slider_step(self):
        step_val = self.slider.get_attribute("step")
        return float(step_val)

    def set_slider_to_value_via_keyboard(self, steps: int):
        self.slider.focus()
        for _ in range(steps):
            self.slider.press("ArrowRight")

    def set_slider_to_value(self, target_value: float) -> None:
        current = float(self.slider.get_attribute("value"))
        steps = round((target_value - current) / self._get_slider_step())

        logger.info(f"{self.slider}: set value from {current} to {target_value}")

        if steps == 0:
            return

        self.slider.wait_for(state="visible")
        self.slider.focus()
        for _ in range(abs(steps)):
            self.slider.press("ArrowRight" if steps > 0 else "ArrowLeft")

    def get_slider_value(self):
        return self.slider_value.get_text_content().strip()

    def generate_random_value(self):

        min_val = self._get_slider_min()
        max_val = self._get_slider_max()
        step = self._get_slider_step()

        max_steps = int((max_val - min_val) / step)
        random_steps = random.randint(0, max_steps)

        return min_val + (random_steps * step)
