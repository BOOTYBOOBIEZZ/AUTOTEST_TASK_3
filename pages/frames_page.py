from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.page_actions import PageActions
from ui.web_element import WebElement


class FramesPage(BasePage):
    URL = "https://the-internet.herokuapp.com/nested_frames"

    def __init__(self, page: Page):
        super().__init__(page)
        self.actions = PageActions(page)

        self.top_frame = page.frame_locator("frame[name='frame-top']")
        self.bottom_frame = page.frame_locator("frame[name='frame-bottom']")

        self.left_frame = self.top_frame.frame_locator("frame[name='frame-left']")
        self.middle_frame = self.top_frame.frame_locator("frame[name='frame-middle']")
        self.right_frame = self.top_frame.frame_locator("frame[name='frame-right']")

        self.left_frame_text = WebElement(
            locator=self.left_frame.locator("body"),
            description="Левая рамка",
            page=page,
        )

        self.middle_frame_text = WebElement(
            locator=self.middle_frame.locator("body"),
            description="Текст в средней рамке",
            page=page,
        )

        self.right_frame_text = WebElement(
            locator=self.right_frame.locator("body"),
            description="Текст в правой рамке",
            page=page,
        )

        self.bottom_frame_text = WebElement(
            locator=self.bottom_frame.locator("body"),
            description="Текст в нижней рамке",
            page=page,
        )

    def open(self):
        self.page.goto(self.URL)

    def hover_on_frame(self, frame: WebElement):
        frame.hover()

    def get_left_frame_text(self):
        return self.actions.get_text(self.left_frame_text)

    def get_right_frame_text(self):
        return self.actions.get_text(self.right_frame_text)

    def get_middle_frame_text(self):
        return self.actions.get_text(self.middle_frame_text)

    def get_bottom_frame_text(self):
        return self.actions.get_text(self.bottom_frame_text)
