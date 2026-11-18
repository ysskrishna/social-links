"""Tests for Mercari platform."""
import pytest


class TestMercari:
    """Test Mercari platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://jp.mercari.com/item/m12345",
            "https://jp.mercari.com/user/profile/abc",
        ],
    )
    def test_mercari_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("mercari", url) is False
        assert sl.detect_platform(url) != "mercari"
