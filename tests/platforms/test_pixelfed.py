"""Tests for Pixelfed platform."""
import pytest


class TestPixelfed:
    """Test Pixelfed platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://pixelfed.social/@dansup", "https://pixelfed.social/dansup"),
        ],
    )
    def test_pixelfed_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "pixelfed"
        assert sl.is_valid("pixelfed", url) is True
        assert sl.sanitize("pixelfed", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://pixelfed.social/p/dansup/123",
            "https://pixelfed.social/discover",
            "https://pixelfed.social/i/web",
        ],
    )
    def test_pixelfed_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("pixelfed", url) is False
        assert sl.detect_platform(url) != "pixelfed"
