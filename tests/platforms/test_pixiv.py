"""Tests for Pixiv platform."""
import pytest


class TestPixiv:
    """Test Pixiv platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.pixiv.net/users/11", "https://www.pixiv.net/users/11"),
            ("https://www.pixiv.net/member.php?id=11", "https://www.pixiv.net/users/11"),
        ],
    )
    def test_pixiv_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "pixiv"
        assert sl.is_valid("pixiv", url) is True
        assert sl.sanitize("pixiv", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.pixiv.net/en/artworks/12345",
            "https://www.pixiv.net/users/11/illustrations",
            "https://www.pixiv.net/users/abc",
        ],
    )
    def test_pixiv_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("pixiv", url) is False
        assert sl.detect_platform(url) != "pixiv"
