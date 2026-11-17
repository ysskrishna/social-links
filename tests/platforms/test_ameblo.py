"""Tests for Ameba Blog platform."""
import pytest


class TestAmeblo:
    """Test Ameba Blog platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://ameblo.jp/ameba-official/entry-12345.html",
            "https://ameblo.jp/ranking",
        ],
    )
    def test_ameblo_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("ameblo", url) is False
        assert sl.detect_platform(url) != "ameblo"
