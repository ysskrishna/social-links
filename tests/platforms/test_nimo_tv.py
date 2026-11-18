"""Tests for Nimo TV platform."""
import pytest


class TestNimoTv:
    """Test Nimo TV platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.nimo.tv/game/123",
        ],
    )
    def test_nimo_tv_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("nimo_tv", url) is False
        assert sl.detect_platform(url) != "nimo_tv"
