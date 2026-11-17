"""Tests for Ko-fi platform."""
import pytest


class TestKoFi:
    """Test Ko-fi platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://ko-fi.com/ysskrishna/shop",
            "https://ko-fi.com/explore",
            "https://ko-fi.com/manage",
        ],
    )
    def test_ko_fi_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("ko_fi", url) is False
        assert sl.detect_platform(url) != "ko_fi"
