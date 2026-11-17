"""Tests for OpenStreetMap platform."""
import pytest


class TestOpenstreetmap:
    """Test OpenStreetMap platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.openstreetmap.org/user/SteveC", "https://www.openstreetmap.org/user/SteveC"),
        ],
    )
    def test_openstreetmap_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "openstreetmap"
        assert sl.is_valid("openstreetmap", url) is True
        assert sl.sanitize("openstreetmap", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.openstreetmap.org/user/SteveC/history",
            "https://www.openstreetmap.org/way/123",
        ],
    )
    def test_openstreetmap_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("openstreetmap", url) is False
        assert sl.detect_platform(url) != "openstreetmap"
