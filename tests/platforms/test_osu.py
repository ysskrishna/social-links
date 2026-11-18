import pytest


class TestOsu:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://osu.ppy.sh/u/peppy", "https://osu.ppy.sh/users/peppy"),
            ("https://osu.ppy.sh/users/2/osu", "https://osu.ppy.sh/users/2"),
        ],
    )
    def test_osu_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "osu"
        assert sl.is_valid("osu", url) is True
        assert sl.sanitize("osu", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://osu.ppy.sh/beatmapsets/1",
            "https://osu.ppy.sh/users/2/scores",
        ],
    )
    def test_osu_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("osu", url) is False
        assert sl.detect_platform(url) != "osu"
