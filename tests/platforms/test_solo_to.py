"""Tests for solo.to platform."""
import pytest


class TestSoloTo:
    """Test solo.to platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://solo.to/pricing",
            "https://solo.to/ysskrishna/abc",
        ],
    )
    def test_solo_to_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("solo_to", url) is False
        assert sl.detect_platform(url) != "solo_to"
