"""Tests for Beacons platform."""
import pytest


class TestBeacons:
    """Test Beacons platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://beacons.ai/ysskrishna/store",
            "https://beacons.ai/pricing",
            "https://beacons.ai/login",
        ],
    )
    def test_beacons_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("beacons", url) is False
        assert sl.detect_platform(url) != "beacons"
