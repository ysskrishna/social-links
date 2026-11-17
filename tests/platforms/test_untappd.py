"""Tests for Untappd platform."""
import pytest


class TestUntappd:
    """Test Untappd platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://untappd.com/user/CiderBeer/photos",
            "https://untappd.com/b/some-beer/123",
        ],
    )
    def test_untappd_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("untappd", url) is False
        assert sl.detect_platform(url) != "untappd"
