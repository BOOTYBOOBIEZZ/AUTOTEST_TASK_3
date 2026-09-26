import pytest

from pages.hovers_page import HoversPage


class TestHoversPage:
    @pytest.mark.parametrize(
        "index, expected_name",
        [
            (0, "name: user1"),
            (1, "name: user2"),
            (2, "name: user3"),
        ],
    )
    def test_get_username(
        self, hovers_page: HoversPage, index: int, expected_name: str
    ):

        hovers_page.hover_user(index)
        actual_name = hovers_page.get_username(index)

        assert actual_name == expected_name, (
            f"Expected '{expected_name}', but got'{actual_name}'"
        )
