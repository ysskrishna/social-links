"""Tests for Kick platform."""
import pytest


class TestKick:
    """Test Kick platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://kick.com/xqc/videos/abc",
            "https://kick.com/categories",
            "https://kick.com/browse",
        ],
    )
    def test_kick_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("kick", url) is False
        assert sl.detect_platform(url) != "kick"
