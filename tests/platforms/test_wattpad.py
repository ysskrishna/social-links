"""Tests for Wattpad platform."""
import pytest


class TestWattpad:
    """Test Wattpad platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.wattpad.com/story/12345-title",
            "https://www.wattpad.com/user/Wattpad/following",
        ],
    )
    def test_wattpad_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("wattpad", url) is False
        assert sl.detect_platform(url) != "wattpad"
