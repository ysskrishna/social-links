"""Tests for Liberapay platform."""
import pytest


class TestLiberapay:
    """Test Liberapay platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://liberapay.com/Liberapay/donate",
        ],
    )
    def test_liberapay_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("liberapay", url) is False
        assert sl.detect_platform(url) != "liberapay"
