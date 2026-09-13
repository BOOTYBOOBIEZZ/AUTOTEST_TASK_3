import pytest
from playwright.sync_api import Page

from pages.hovers_page import HoversPage, Users
from ui.page_actions import PageActions


class TestHoversPage:
    URL = "https://the-internet.herokuapp.com/hovers"

    @pytest.mark.parametrize("user", [Users.USER_1, Users.USER_2, Users.USER_3])
    def test_hovers(self, page: Page, user: Users):

        hovers_page = HoversPage(page)
        self.actions = PageActions(page)

        hovers_page.open()

        user_mapping = {
            Users.USER_1: {
                "avatar": hovers_page.avatar_1,
                "name_element": hovers_page.user_1,
                "expected_name": "name: user1",
            },
            Users.USER_2: {
                "avatar": hovers_page.avatar_2,
                "name_element": hovers_page.user_2,
                "expected_name": "name: user2",
            },
            Users.USER_3: {
                "avatar": hovers_page.avatar_3,
                "name_element": hovers_page.user_3,
                "expected_name": "name: user3",
            },
        }

        data = user_mapping[user]
        avatar = data["avatar"]
        name_element = data["name_element"]
        expected_name = data["expected_name"]

        hovers_page.hover_on_image(avatar)

        actual_name = hovers_page.get_user_name(name_element)

        assert actual_name == expected_name, (
            "Expected '{expected_name}', but got'{actual_name}'"
        )
