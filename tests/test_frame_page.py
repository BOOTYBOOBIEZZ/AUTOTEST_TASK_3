import pytest

from pages.frames_page import FramesPage
from utils.frame_name import FrameName


class TestFramesPage:
    @pytest.mark.parametrize(
        "frame_name, expected_text",
        [
            (FrameName.LEFT, "LEFT"),
            (FrameName.MIDDLE, "MIDDLE"),
            (FrameName.RIGHT, "RIGHT"),
            (FrameName.BOTTOM, "BOTTOM"),
        ],
    )
    def test_frame_text(
        self,
        frames_page: FramesPage,
        frame_name: FrameName,
        expected_text: str,
    ):

        actual_text = frames_page.get_frame_text(frame_name)

        assert actual_text == expected_text, (
            f"AssertionError in '{frame_name}. /n"
            f"Expected: '{expected_text}', but got '{actual_text}'."
        )
