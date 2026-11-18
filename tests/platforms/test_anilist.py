"""Tests for AniList platform."""
import pytest


class TestAnilist:
    """Test AniList platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://anilist.co/anime/1/Cowboy-Bebop",
            "https://anilist.co/user/Josh/animelist",
        ],
    )
    def test_anilist_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("anilist", url) is False
        assert sl.detect_platform(url) != "anilist"
