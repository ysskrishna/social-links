import pytest


class TestStackExchange:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://stackexchange.com/users/1", "https://stackexchange.com/users/1"),
        ],
    )
    def test_stack_exchange_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "stack_exchange"
        assert sl.is_valid("stack_exchange", url) is True
        assert sl.sanitize("stack_exchange", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://stackexchange.com/users/jeff-atwood",
            "https://stackexchange.com/sites",
            "https://math.stackexchange.com/users/1/jeff-atwood",
        ],
    )
    def test_stack_exchange_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("stack_exchange", url) is False
        assert sl.detect_platform(url) != "stack_exchange"
