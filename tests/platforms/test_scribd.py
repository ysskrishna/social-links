import pytest


class TestScribd:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.scribd.com/document/123/title",
            "https://www.scribd.com/user/trip",
        ],
    )
    def test_scribd_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("scribd", url) is False
        assert sl.detect_platform(url) != "scribd"
