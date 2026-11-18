"""Tests for XING platform."""
import pytest


class TestXing:
    """Test XING platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.xing.com/profile/Thomas_Vollmoeller/cv", "https://www.xing.com/profile/Thomas_Vollmoeller"),
        ],
    )
    def test_xing_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "xing"
        assert sl.is_valid("xing", url) is True
        assert sl.sanitize("xing", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.xing.com/jobs/berlin",
            "https://www.xing.com/pages/xing",
        ],
    )
    def test_xing_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("xing", url) is False
        assert sl.detect_platform(url) != "xing"
