"""Tests for OnlyFans platform."""
import pytest


class TestOnlyfans:
    """Test OnlyFans platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://onlyfans.com/my/notifications",
            "https://onlyfans.com/onlyfans/c12",
            "https://onlyfans.com/action/trial/abc",
            "https://onlyfans.com/help",
        ],
    )
    def test_onlyfans_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("onlyfans", url) is False
        assert sl.detect_platform(url) != "onlyfans"
