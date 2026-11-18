import pytest


class TestMinds:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.minds.com/newsfeed/1234567890",
            "https://www.minds.com/minds/blog",
        ],
    )
    def test_minds_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("minds", url) is False
        assert sl.detect_platform(url) != "minds"
