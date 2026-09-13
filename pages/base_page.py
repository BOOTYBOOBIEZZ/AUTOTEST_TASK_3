from typing import Type, TypeVar  # noqa: UP035

from playwright.sync_api import Page

from ui.page_actions import PageActions

T = TypeVar("T", bound="BasePage")


class BasePage:
    def __init__(self, page: Page):
        self.actions = PageActions(page)
        self.page = page

    def get_page(self, page_class: type[T]) -> T:
        return page_class(self.page)
