from playwright.sync_api import Page

from pages.base_page import BasePage
from ui.multi_web_element import MultiWebElement


class DynamicContentPage(BasePage):
    URL = "https://the-internet.herokuapp.com/dynamic_content"

    def __init__(self, page: Page):
        super().__init__(page)

        self.images = MultiWebElement(
            locator=page.locator("img[src^='/img/avatars/']"),
            description="images",
            page=page,
        )

    def open(self):
        self.actions.goto(self.URL)

    def get_img_srcs(self):
        return [img.get_attribute("src") for img in self.images.all()]

    def get_image_count(self):
        return self.images.count()

    def find_same_images(self):
        srcs = self.get_img_srcs()
        seen = set()
        duplicates = set()

        for src in srcs:
            if src in seen:
                duplicates.add(src)
            seen.add(src)

        return list(duplicates)

    def has_duplicate_images(self) -> bool:
        return len(self.find_same_images()) > 0

    def refresh_until_duplicates(self, max_attempts: int = 10):
        for attempt in range(max_attempts):
            if self.has_duplicate_images():
                print(f"Duplicates found after {attempt + 1} attempt(s)!")
                return True
            else:
                self.page.reload()
                self.images.locator.first.wait_for(state="visible")
