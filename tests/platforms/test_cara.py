"""Tests for Cara platform."""
import pytest


class TestCara:
    """Test Cara platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://cara.app/post/abc",
            "https://cara.app/ysskrishna/all",
        ],
    )
    def test_cara_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("cara", url) is False
        assert sl.detect_platform(url) != "cara"
