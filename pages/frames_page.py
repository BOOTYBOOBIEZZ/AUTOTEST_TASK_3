from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement


class FramesPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.top_frame = page.frame_locator("frame[name='frame-top']")
        self.bottom_frame = page.frame_locator("frame[name='frame-bottom']")

        self.left_frame = self.top_frame.frame_locator("frame[name='frame-left']")
        self.middle_frame = self.top_frame.frame_locator("frame[name='frame-middle']")
        self.right_frame = self.top_frame.frame_locator("frame[name='frame-right']")

        self._left_frame_text = WebElement(
            locator=self.left_frame.locator("body"),
            description="Левая рамка",
            page=page,
        )

        self._middle_frame_text = WebElement(
            locator=self.middle_frame.locator("body"),
            description="Текст в средней рамке",
            page=page,
        )

        self._right_frame_text = WebElement(
            locator=self.right_frame.locator("body"),
            description="Текст в правой рамке",
            page=page,
        )

        self._bottom_frame_text = WebElement(
            locator=self.bottom_frame.locator("body"),
            description="Текст в нижней рамке",
            page=page,
        )

    def get_left_frame_text(self):
        return self.actions.get_text(self._left_frame_text)

    def get_right_frame_text(self):
        return self.actions.get_text(self._right_frame_text)

    def get_middle_frame_text(self):
        return self.actions.get_text(self._middle_frame_text)

    def get_bottom_frame_text(self):
        return self.actions.get_text(self._bottom_frame_text)

    def get_frame_text(self, frame_name: str):
        frames = {
            "left": self._left_frame_text,
            "right": self._right_frame_text,
            "middle": self._middle_frame_text,
            "bottom": self._bottom_frame_text,
        }
        if frame_name not in frames:
            raise ValueError
        return frames[frame_name].get_inner_text()
