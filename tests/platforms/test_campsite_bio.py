"""Tests for Campsite.bio platform."""
import pytest


class TestCampsiteBio:
    """Test Campsite.bio platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://campsite.bio/pricing",
            "https://campsite.bio/ysskrishna/abc",
        ],
    )
    def test_campsite_bio_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("campsite_bio", url) is False
        assert sl.detect_platform(url) != "campsite_bio"
