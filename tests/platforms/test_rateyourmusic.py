import pytest


class TestRateyourmusic:
    @pytest.mark.parametrize(
        "url",
        [
            "https://rateyourmusic.com/artist/radiohead",
            "https://rateyourmusic.com/Jarevo",
        ],
    )
    def test_rateyourmusic_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("rateyourmusic", url) is False
        assert sl.detect_platform(url) != "rateyourmusic"
