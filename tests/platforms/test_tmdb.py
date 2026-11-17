"""Tests for TMDB platform."""
import pytest


class TestTmdb:
    """Test TMDB platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.themoviedb.org/movie/550-fight-club",
            "https://www.themoviedb.org/u/travisbell/lists",
        ],
    )
    def test_tmdb_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("tmdb", url) is False
        assert sl.detect_platform(url) != "tmdb"
