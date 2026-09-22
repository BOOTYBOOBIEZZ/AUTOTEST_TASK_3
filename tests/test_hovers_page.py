import pytest
from playwright.sync_api import Page

from pages.hovers_page import HoversPage
from utils.url_utils import HOVERS_URL


class TestHoversPage:
    @pytest.mark.parametrize(
        "index, expected_name",
        [
            (0, "name: user1"),
            (1, "name: user2"),
            (2, "name: user3"),
        ],
    )
    def test_get_username(self, page: Page, index: int, expected_name: str):

        hovers_page = HoversPage(page)

        hovers_page.open(HOVERS_URL)

        hovers_page.hover_user(index)
        actual_name = hovers_page.get_username(index)

        assert actual_name == expected_name, (
            "Expected '{expected_name}', but got'{actual_name}'"
        )
