"""Tests for eBay platform."""
import pytest


class TestEbay:
    """Test eBay platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.ebay.co.uk/usr/ysskrishna", "https://www.ebay.com/usr/ysskrishna"),
        ],
    )
    def test_ebay_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "ebay"
        assert sl.is_valid("ebay", url) is True
        assert sl.sanitize("ebay", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.ebay.com/itm/123456789",
            "https://www.ebay.com.evil.io/usr/ysskrishna",
            "https://www.ebay.com/str/someshop",
        ],
    )
    def test_ebay_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("ebay", url) is False
        assert sl.detect_platform(url) != "ebay"
