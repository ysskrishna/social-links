import pytest


class TestGoodreads:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.goodreads.com/user/show/1", "https://www.goodreads.com/user/show/1"),
        ],
    )
    def test_goodreads_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "goodreads"
        assert sl.is_valid("goodreads", url) is True
        assert sl.sanitize("goodreads", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.goodreads.com/book/show/5907.The_Hobbit",
            "https://www.goodreads.com/user/show/otis",
        ],
    )
    def test_goodreads_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("goodreads", url) is False
        assert sl.detect_platform(url) != "goodreads"
