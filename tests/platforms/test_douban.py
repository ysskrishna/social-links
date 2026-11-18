import pytest


class TestDouban:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://m.douban.com/people/1000001/", "https://www.douban.com/people/1000001"),
        ],
    )
    def test_douban_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "douban"
        assert sl.is_valid("douban", url) is True
        assert sl.sanitize("douban", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://movie.douban.com/subject/1292052/",
            "https://www.douban.com/people/ahbei/statuses",
        ],
    )
    def test_douban_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("douban", url) is False
        assert sl.detect_platform(url) != "douban"
