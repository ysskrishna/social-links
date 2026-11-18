import pytest


class TestHabr:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://habr.com/en/users/boomburum", "https://habr.com/users/boomburum"),
            ("https://habr.com/users/boomburum", "https://habr.com/users/boomburum"),
        ],
    )
    def test_habr_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "habr"
        assert sl.is_valid("habr", url) is True
        assert sl.sanitize("habr", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://habr.com/ru/users/boomburum/posts/",
            "https://habr.com/ru/articles/123456/",
        ],
    )
    def test_habr_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("habr", url) is False
        assert sl.detect_platform(url) != "habr"
