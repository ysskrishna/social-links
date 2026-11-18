"""Tests for Taplink platform."""
import pytest


class TestTaplink:
    """Test Taplink platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://taplink.at/ysskrishna", "https://taplink.cc/ysskrishna"),
        ],
    )
    def test_taplink_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "taplink"
        assert sl.is_valid("taplink", url) is True
        assert sl.sanitize("taplink", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://taplink.cc/ysskrishna/p/abc",
        ],
    )
    def test_taplink_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("taplink", url) is False
        assert sl.detect_platform(url) != "taplink"
