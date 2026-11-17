"""Tests for Brunch platform."""
import pytest


class TestBrunch:
    """Test Brunch platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://brunch.co.kr/@brunch/123",
            "https://brunch.co.kr/keyword/IT",
        ],
    )
    def test_brunch_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("brunch", url) is False
        assert sl.detect_platform(url) != "brunch"
