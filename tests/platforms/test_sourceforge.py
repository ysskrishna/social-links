"""Tests for SourceForge platform."""
import pytest


class TestSourceforge:
    """Test SourceForge platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://sourceforge.net/u/rspeed/", "https://sourceforge.net/u/rspeed/profile"),
        ],
    )
    def test_sourceforge_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "sourceforge"
        assert sl.is_valid("sourceforge", url) is True
        assert sl.sanitize("sourceforge", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://sourceforge.net/projects/sevenzip/",
            "https://sourceforge.net/u/rspeed/wiki",
        ],
    )
    def test_sourceforge_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("sourceforge", url) is False
        assert sl.detect_platform(url) != "sourceforge"
