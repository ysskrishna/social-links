"""Tests for Indie Hackers platform."""
import pytest


class TestIndiehackers:
    """Test Indie Hackers platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.indiehackers.com/post/some-title-abc123",
            "https://www.indiehackers.com/products",
            "https://www.indiehackers.com/csallen/history",
        ],
    )
    def test_indiehackers_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("indiehackers", url) is False
        assert sl.detect_platform(url) != "indiehackers"
