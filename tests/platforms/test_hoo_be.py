"""Tests for Hoo.be platform."""
import pytest


class TestHooBe:
    """Test Hoo.be platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://hoo.be/login",
            "https://hoo.be/ysskrishna/abc",
        ],
    )
    def test_hoo_be_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("hoo_be", url) is False
        assert sl.detect_platform(url) != "hoo_be"
