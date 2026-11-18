import pytest


class TestHackerearth:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.hackerearth.com/challenges/",
            "https://www.hackerearth.com/@sachin/activity",
        ],
    )
    def test_hackerearth_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("hackerearth", url) is False
        assert sl.detect_platform(url) != "hackerearth"
