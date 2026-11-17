"""Tests for Komoot platform."""
import pytest


class TestKomoot:
    """Test Komoot platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.komoot.com/de-de/user/1234567890", "https://www.komoot.com/user/1234567890"),
        ],
    )
    def test_komoot_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "komoot"
        assert sl.is_valid("komoot", url) is True
        assert sl.sanitize("komoot", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.komoot.com/tour/123",
            "https://www.komoot.com/user/ysskrishna/tours",
        ],
    )
    def test_komoot_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("komoot", url) is False
        assert sl.detect_platform(url) != "komoot"
