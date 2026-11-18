"""Tests for Issuu platform."""
import pytest


class TestIssuu:
    """Test Issuu platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://issuu.com/issuu/docs/report",
        ],
    )
    def test_issuu_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("issuu", url) is False
        assert sl.detect_platform(url) != "issuu"
