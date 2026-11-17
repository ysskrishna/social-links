"""Tests for Mixcloud platform."""
import pytest


class TestMixcloud:
    """Test Mixcloud platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.mixcloud.com/NTSRadio/show-name-01-01-2024/",
        ],
    )
    def test_mixcloud_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("mixcloud", url) is False
        assert sl.detect_platform(url) != "mixcloud"
