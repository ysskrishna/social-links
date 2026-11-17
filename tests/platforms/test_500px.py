"""Tests for 500px platform."""
import pytest


class Test500px:
    """Test 500px platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://500px.com/photo/123/title",
            "https://500px.com/p/ysskrishna/likes",
        ],
    )
    def test_500px_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("500px", url) is False
        assert sl.detect_platform(url) != "500px"
