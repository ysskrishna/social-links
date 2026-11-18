import pytest


class TestPoshmark:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://poshmark.ca/closet/ysskrishna", "https://poshmark.com/closet/ysskrishna"),
        ],
    )
    def test_poshmark_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "poshmark"
        assert sl.is_valid("poshmark", url) is True
        assert sl.sanitize("poshmark", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://poshmark.com/listing/abc-123",
            "https://poshmark.com/closet/ysskrishna/likes",
        ],
    )
    def test_poshmark_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("poshmark", url) is False
        assert sl.detect_platform(url) != "poshmark"
