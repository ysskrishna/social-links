"""Tests for Jamendo platform."""
import pytest


class TestJamendo:
    """Test Jamendo platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.jamendo.com/user/1", "https://www.jamendo.com/user/1"),
            ("https://www.jamendo.com/user/mahoosy", "https://www.jamendo.com/user/mahoosy"),
        ],
    )
    def test_jamendo_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "jamendo"
        assert sl.is_valid("jamendo", url) is True
        assert sl.sanitize("jamendo", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.jamendo.com/track/123/song",
            "https://www.jamendo.com/user/mahoosy/playlists",
        ],
    )
    def test_jamendo_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("jamendo", url) is False
        assert sl.detect_platform(url) != "jamendo"
