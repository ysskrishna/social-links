import pytest


class TestDzen:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://dzen.ru/id/5a1c2b3d4e5f60718293a4b5", "https://dzen.ru/id/5a1c2b3d4e5f60718293a4b5"),
            ("https://zen.yandex.ru/dzen", "https://dzen.ru/dzen"),
        ],
    )
    def test_dzen_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "dzen"
        assert sl.is_valid("dzen", url) is True
        assert sl.sanitize("dzen", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://dzen.ru/a/ZabcDEF",
            "https://dzen.ru/dzen/article",
        ],
    )
    def test_dzen_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("dzen", url) is False
        assert sl.detect_platform(url) != "dzen"
