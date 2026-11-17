"""Tests for Malt platform."""
import pytest


class TestMalt:
    """Test Malt platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.malt.de/profile/ysskrishna", "https://www.malt.fr/profile/ysskrishna"),
        ],
    )
    def test_malt_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "malt"
        assert sl.is_valid("malt", url) is True
        assert sl.sanitize("malt", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.malt.fr/s?q=python",
            "https://www.malt.fr/profile/ysskrishna/portfolio",
        ],
    )
    def test_malt_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("malt", url) is False
        assert sl.detect_platform(url) != "malt"
