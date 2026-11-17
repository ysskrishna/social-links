"""Tests for Pexels platform."""
import pytest


class TestPexels:
    """Test Pexels platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.pexels.com/de-de/@pexels", "https://www.pexels.com/@pexels"),
        ],
    )
    def test_pexels_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "pexels"
        assert sl.is_valid("pexels", url) is True
        assert sl.sanitize("pexels", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.pexels.com/photo/abc-123/",
            "https://www.pexels.com/@pexels/collections",
        ],
    )
    def test_pexels_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("pexels", url) is False
        assert sl.detect_platform(url) != "pexels"
