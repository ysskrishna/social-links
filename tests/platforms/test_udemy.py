"""Tests for Udemy platform."""
import pytest


class TestUdemy:
    """Test Udemy platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.udemy.com/course/python/",
            "https://www.udemy.com/user/",
        ],
    )
    def test_udemy_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("udemy", url) is False
        assert sl.detect_platform(url) != "udemy"
