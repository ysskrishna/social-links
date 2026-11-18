"""Tests for Carrd platform."""
import pytest


class TestCarrd:
    """Test Carrd platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://carrd.co/",
            "https://www.carrd.co/",
            "https://ysskrishna.carrd.co.evil.io/",
        ],
    )
    def test_carrd_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("carrd", url) is False
        assert sl.detect_platform(url) != "carrd"
