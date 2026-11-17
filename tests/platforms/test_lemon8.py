"""Tests for Lemon8 platform."""
import pytest


class TestLemon8:
    """Test Lemon8 platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.lemon8-app.com/@lemon8us/7123456789",
            "https://www.lemon8-app.com/discover",
        ],
    )
    def test_lemon8_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("lemon8", url) is False
        assert sl.detect_platform(url) != "lemon8"
