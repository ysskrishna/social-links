"""Tests for GOG platform."""
import pytest


class TestGog:
    """Test GOG platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.gog.com/en/u/ysskrishna", "https://www.gog.com/u/ysskrishna"),
        ],
    )
    def test_gog_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "gog"
        assert sl.is_valid("gog", url) is True
        assert sl.sanitize("gog", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.gog.com/en/game/the_witcher_3",
            "https://www.gog.com/u/ysskrishna/games",
        ],
    )
    def test_gog_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("gog", url) is False
        assert sl.detect_platform(url) != "gog"
