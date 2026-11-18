"""Tests for Letterboxd platform."""
import pytest


class TestLetterboxd:
    """Test Letterboxd platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://letterboxd.com/film/parasite-2019/",
            "https://letterboxd.com/davidehrlich/films/",
        ],
    )
    def test_letterboxd_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("letterboxd", url) is False
        assert sl.detect_platform(url) != "letterboxd"
