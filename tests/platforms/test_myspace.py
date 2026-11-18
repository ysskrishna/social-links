import pytest


class TestMyspace:
    @pytest.mark.parametrize(
        "url",
        [
            "https://myspace.com/tom/music/songs",
        ],
    )
    def test_myspace_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("myspace", url) is False
        assert sl.detect_platform(url) != "myspace"
