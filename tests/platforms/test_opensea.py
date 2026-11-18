import pytest


class TestOpensea:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://opensea.io/ysskrishna", "https://opensea.io/ysskrishna"),
        ],
    )
    def test_opensea_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "opensea"
        assert sl.is_valid("opensea", url) is True
        assert sl.sanitize("opensea", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://opensea.io/collection/boredapeyachtclub",
            "https://opensea.io/assets/ethereum/0xabc/1",
        ],
    )
    def test_opensea_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("opensea", url) is False
        assert sl.detect_platform(url) != "opensea"
