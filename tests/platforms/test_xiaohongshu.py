"""Tests for Xiaohongshu (RedNote) platform."""
import pytest


class TestXiaohongshu:
    """Test Xiaohongshu (RedNote) platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.rednote.com/user/profile/5ff0e6410000000001008400?xsec_token=abc", "https://www.rednote.com/user/profile/5ff0e6410000000001008400"),
        ],
    )
    def test_xiaohongshu_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "xiaohongshu"
        assert sl.is_valid("xiaohongshu", url) is True
        assert sl.sanitize("xiaohongshu", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.xiaohongshu.com/explore/64a1",
            "https://www.xiaohongshu.com/user/profile/",
        ],
    )
    def test_xiaohongshu_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("xiaohongshu", url) is False
        assert sl.detect_platform(url) != "xiaohongshu"
