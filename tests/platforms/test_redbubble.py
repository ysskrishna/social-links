"""Tests for Redbubble platform."""
import pytest


class TestRedbubble:
    """Test Redbubble platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.redbubble.com/people/ysskrishna", "https://www.redbubble.com/people/ysskrishna"),
        ],
    )
    def test_redbubble_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "redbubble"
        assert sl.is_valid("redbubble", url) is True
        assert sl.sanitize("redbubble", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.redbubble.com/i/t-shirt/abc/123",
            "https://www.redbubble.com/people/ysskrishna/works/123",
        ],
    )
    def test_redbubble_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("redbubble", url) is False
        assert sl.detect_platform(url) != "redbubble"
