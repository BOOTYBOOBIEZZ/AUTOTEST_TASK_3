import pytest

from pages.frames_page import FramesPage


class TestFramesPage:
    FRAME_TEST_DATA = (
        ("left", "LEFT", "get_left_frame_text"),
        ("middle", "MIDDLE", "get_middle_frame_text"),
        ("right", "RIGHT", "get_right_frame_text"),
        ("bottom", "BOTTOM", "get_bottom_frame_text"),
    )

    @pytest.mark.parametrize("frame_name, expected_text, method_name", FRAME_TEST_DATA)
    def test_frame_text(
        self,
        frames_page: FramesPage,
        frame_name: str,
        expected_text: str,
        method_name: str,
    ):

        get_text_method = getattr(frames_page, method_name)
        actual_text = get_text_method()

        assert actual_text == expected_text, (
            f"AssertionError in '{frame_name}. /n"
            f"Expected: '{expected_text}', but got '{actual_text}'."
        )
