"""Tests for Last.fm platform."""
import pytest


class TestLastfm:
    """Test Last.fm platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.last.fm/de/user/RJ", "https://www.last.fm/user/RJ"),
        ],
    )
    def test_lastfm_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "lastfm"
        assert sl.is_valid("lastfm", url) is True
        assert sl.sanitize("lastfm", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.last.fm/music/Radiohead",
            "https://www.last.fm/user/RJ/library",
        ],
    )
    def test_lastfm_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("lastfm", url) is False
        assert sl.detect_platform(url) != "lastfm"
