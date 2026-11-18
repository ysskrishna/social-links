import pytest


class TestLine:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://line.me/R/ti/p/@linejapan", "https://page.line.me/linejapan"),
            ("https://line.me/R/ti/p/%40linejapan", "https://page.line.me/linejapan"),
        ],
    )
    def test_line_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "line"
        assert sl.is_valid("line", url) is True
        assert sl.sanitize("line", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://line.me/R/ti/p/~personal",
            "https://page.line.me/linejapan/post/123",
            "https://line.me/en/",
        ],
    )
    def test_line_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("line", url) is False
        assert sl.detect_platform(url) != "line"
