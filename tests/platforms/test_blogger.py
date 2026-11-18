"""Tests for Blogger platform."""
import pytest


class TestBlogger:
    """Test Blogger platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.blogger.com/about/",
            "https://www.blogger.com/profile/abc",
        ],
    )
    def test_blogger_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("blogger", url) is False
        assert sl.detect_platform(url) != "blogger"
