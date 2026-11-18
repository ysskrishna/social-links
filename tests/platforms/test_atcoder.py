"""Tests for AtCoder platform."""
import pytest


class TestAtcoder:
    """Test AtCoder platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://atcoder.jp/users/tourist?lang=en", "https://atcoder.jp/users/tourist"),
        ],
    )
    def test_atcoder_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "atcoder"
        assert sl.is_valid("atcoder", url) is True
        assert sl.sanitize("atcoder", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://atcoder.jp/users/tourist/history",
            "https://atcoder.jp/contests/abc300",
        ],
    )
    def test_atcoder_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("atcoder", url) is False
        assert sl.detect_platform(url) != "atcoder"
