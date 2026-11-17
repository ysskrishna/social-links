"""Tests for KakaoTalk Channel platform."""
import pytest


class TestKakaotalkChannel:
    """Test KakaoTalk Channel platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://pf.kakao.com/_xfxhcWs/posts", "https://pf.kakao.com/_xfxhcWs"),
        ],
    )
    def test_kakaotalk_channel_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "kakaotalk_channel"
        assert sl.is_valid("kakaotalk_channel", url) is True
        assert sl.sanitize("kakaotalk_channel", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://pf.kakao.com/xfxhcWs",
            "https://pf.kakao.com/_xfxhcWs/12345",
        ],
    )
    def test_kakaotalk_channel_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("kakaotalk_channel", url) is False
        assert sl.detect_platform(url) != "kakaotalk_channel"
