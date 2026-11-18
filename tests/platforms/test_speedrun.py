import pytest


class TestSpeedrun:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.speedrun.com/user/cheese", "https://www.speedrun.com/users/cheese"),
        ],
    )
    def test_speedrun_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "speedrun"
        assert sl.is_valid("speedrun", url) is True
        assert sl.sanitize("speedrun", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.speedrun.com/sm64",
            "https://www.speedrun.com/users/cheese/runs",
        ],
    )
    def test_speedrun_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("speedrun", url) is False
        assert sl.detect_platform(url) != "speedrun"
