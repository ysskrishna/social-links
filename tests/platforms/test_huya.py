import pytest


class TestHuya:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.huya.com/100", "https://www.huya.com/100"),
        ],
    )
    def test_huya_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "huya"
        assert sl.is_valid("huya", url) is True
        assert sl.sanitize("huya", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.huya.com/g/lol",
            "https://www.huya.com/uzi/video",
        ],
    )
    def test_huya_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("huya", url) is False
        assert sl.detect_platform(url) != "huya"
