from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.web_element import WebElement
from utils.frame_name import FrameName


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

        self._frames = {
            FrameName.LEFT: self._left_frame_text,
            FrameName.MIDDLE: self._middle_frame_text,
            FrameName.RIGHT: self._right_frame_text,
            FrameName.BOTTOM: self._bottom_frame_text,
        }

    def get_left_frame_text(self):
        return self.actions.get_text(self._left_frame_text)

    def get_right_frame_text(self):
        return self.actions.get_text(self._right_frame_text)

    def get_middle_frame_text(self):
        return self.actions.get_text(self._middle_frame_text)

    def get_bottom_frame_text(self):
        return self.actions.get_text(self._bottom_frame_text)

    def get_frame_text(self, frame_name: FrameName):
        if frame_name not in self._frames:
            raise ValueError(f"Unknown frame: '{frame_name}'. ")
        return self._frames[frame_name].get_inner_text()
