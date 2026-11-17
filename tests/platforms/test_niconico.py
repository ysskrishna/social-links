"""Tests for Niconico platform."""
import pytest


class TestNiconico:
    """Test Niconico platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.nicovideo.jp/watch/sm9",
            "https://www.nicovideo.jp/user/1/video",
        ],
    )
    def test_niconico_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("niconico", url) is False
        assert sl.detect_platform(url) != "niconico"
