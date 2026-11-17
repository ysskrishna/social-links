"""Tests for Flipboard platform."""
import pytest


class TestFlipboard:
    """Test Flipboard platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://flipboard.com/@flipboard/tech-abc123",
            "https://flipboard.com/topic/tech",
        ],
    )
    def test_flipboard_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("flipboard", url) is False
        assert sl.detect_platform(url) != "flipboard"
