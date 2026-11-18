import pytest


class TestFreecodecamp:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://forum.freecodecamp.org/u/QuincyLarson/summary", "https://forum.freecodecamp.org/u/QuincyLarson"),
        ],
    )
    def test_freecodecamp_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "freecodecamp"
        assert sl.is_valid("freecodecamp", url) is True
        assert sl.sanitize("freecodecamp", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://forum.freecodecamp.org/t/some-topic/123",
            "https://forum.freecodecamp.org/u/QuincyLarson/activity",
        ],
    )
    def test_freecodecamp_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("freecodecamp", url) is False
        assert sl.detect_platform(url) != "freecodecamp"
