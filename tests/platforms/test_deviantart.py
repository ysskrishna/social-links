"""Tests for DeviantArt platform."""
import pytest


class TestDeviantart:
    """Test DeviantArt platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://spyed.deviantart.com/", "https://www.deviantart.com/spyed"),
        ],
    )
    def test_deviantart_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "deviantart"
        assert sl.is_valid("deviantart", url) is True
        assert sl.sanitize("deviantart", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.deviantart.com/spyed/art/Some-Art-12345",
        ],
    )
    def test_deviantart_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("deviantart", url) is False
        assert sl.detect_platform(url) != "deviantart"
