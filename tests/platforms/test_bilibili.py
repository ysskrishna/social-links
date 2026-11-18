import pytest


class TestBilibili:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://m.bilibili.com/space/2", "https://space.bilibili.com/2"),
        ],
    )
    def test_bilibili_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "bilibili"
        assert sl.is_valid("bilibili", url) is True
        assert sl.sanitize("bilibili", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.bilibili.com/video/BV1xx411c7mD",
            "https://space.bilibili.com/abc",
            "https://space.bilibili.com/2/video",
        ],
    )
    def test_bilibili_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("bilibili", url) is False
        assert sl.detect_platform(url) != "bilibili"
