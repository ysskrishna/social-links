"""Tests for Douyu platform."""
import pytest


class TestDouyu:
    """Test Douyu platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.douyu.com/22222", "https://www.douyu.com/22222"),
        ],
    )
    def test_douyu_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "douyu"
        assert sl.is_valid("douyu", url) is True
        assert sl.sanitize("douyu", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.douyu.com/directory/all",
            "https://www.douyu.com/22222/video",
        ],
    )
    def test_douyu_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("douyu", url) is False
        assert sl.detect_platform(url) != "douyu"
