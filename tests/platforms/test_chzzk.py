"""Tests for CHZZK platform."""
import pytest


class TestChzzk:
    """Test CHZZK platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://chzzk.naver.com/live/458f6ec20b034f49e0fc6d03921646d2", "https://chzzk.naver.com/458f6ec20b034f49e0fc6d03921646d2"),
        ],
    )
    def test_chzzk_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "chzzk"
        assert sl.is_valid("chzzk", url) is True
        assert sl.sanitize("chzzk", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://chzzk.naver.com/category/GAME/abc",
            "https://chzzk.naver.com/video/123",
            "https://chzzk.naver.com/lives",
        ],
    )
    def test_chzzk_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("chzzk", url) is False
        assert sl.detect_platform(url) != "chzzk"
