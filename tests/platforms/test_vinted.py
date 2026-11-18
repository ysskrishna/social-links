import pytest


class TestVinted:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.vinted.co.uk/member/1", "https://www.vinted.com/member/1"),
        ],
    )
    def test_vinted_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "vinted"
        assert sl.is_valid("vinted", url) is True
        assert sl.sanitize("vinted", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.vinted.fr/items/123-title",
            "https://www.vinted.fr.evil.io/member/1",
        ],
    )
    def test_vinted_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("vinted", url) is False
        assert sl.detect_platform(url) != "vinted"
