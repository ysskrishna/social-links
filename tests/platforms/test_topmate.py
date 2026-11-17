"""Tests for Topmate platform."""
import pytest


class TestTopmate:
    """Test Topmate platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://topmate.io/ysskrishna/12345",
            "https://topmate.io/pricing",
        ],
    )
    def test_topmate_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("topmate", url) is False
        assert sl.detect_platform(url) != "topmate"
