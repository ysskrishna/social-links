"""Tests for Juejin platform."""
import pytest


class TestJuejin:
    """Test Juejin platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://juejin.cn/user/1838039172387262/posts", "https://juejin.cn/user/1838039172387262"),
        ],
    )
    def test_juejin_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "juejin"
        assert sl.is_valid("juejin", url) is True
        assert sl.sanitize("juejin", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://juejin.cn/post/7242693300053655608",
            "https://juejin.cn/user/abc",
        ],
    )
    def test_juejin_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("juejin", url) is False
        assert sl.detect_platform(url) != "juejin"
