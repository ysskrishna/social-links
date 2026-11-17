"""Tests for Hatena Blog platform."""
import pytest


class TestHatenaBlog:
    """Test Hatena Blog platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://staff.hateblo.jp/", "https://staff.hatenablog.com"),
        ],
    )
    def test_hatena_blog_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "hatena_blog"
        assert sl.is_valid("hatena_blog", url) is True
        assert sl.sanitize("hatena_blog", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://staff.hatenablog.com/entry/2024/01/01/000000",
            "https://hatenablog.com/",
        ],
    )
    def test_hatena_blog_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("hatena_blog", url) is False
        assert sl.detect_platform(url) != "hatena_blog"
