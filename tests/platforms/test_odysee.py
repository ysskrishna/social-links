"""Tests for Odysee platform."""
import pytest


class TestOdysee:
    """Test Odysee platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://odysee.com/@Odysee", "https://odysee.com/@Odysee"),
        ],
    )
    def test_odysee_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "odysee"
        assert sl.is_valid("odysee", url) is True
        assert sl.sanitize("odysee", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://odysee.com/@Odysee:8/some-video:1",
            "https://odysee.com/$/help",
        ],
    )
    def test_odysee_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("odysee", url) is False
        assert sl.detect_platform(url) != "odysee"
