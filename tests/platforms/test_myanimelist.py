import pytest


class TestMyanimelist:
    @pytest.mark.parametrize(
        "url",
        [
            "https://myanimelist.net/anime/1/Cowboy_Bebop",
            "https://myanimelist.net/profile/Xinil/reviews",
        ],
    )
    def test_myanimelist_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("myanimelist", url) is False
        assert sl.detect_platform(url) != "myanimelist"
