"""Tests for Buttondown platform."""
import pytest


class TestButtondown:
    """Test Buttondown platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://buttondown.email/ysskrishna", "https://buttondown.com/ysskrishna"),
        ],
    )
    def test_buttondown_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "buttondown"
        assert sl.is_valid("buttondown", url) is True
        assert sl.sanitize("buttondown", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://buttondown.com/ysskrishna/archive/post-slug/",
            "https://buttondown.com/features",
            "https://buttondown.com/pricing",
        ],
    )
    def test_buttondown_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("buttondown", url) is False
        assert sl.detect_platform(url) != "buttondown"
