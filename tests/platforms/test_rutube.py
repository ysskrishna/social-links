"""Tests for Rutube platform."""
import pytest


class TestRutube:
    """Test Rutube platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://rutube.ru/channel/23704195/videos/", "https://rutube.ru/channel/23704195"),
        ],
    )
    def test_rutube_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "rutube"
        assert sl.is_valid("rutube", url) is True
        assert sl.sanitize("rutube", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://rutube.ru/video/abc123/",
            "https://rutube.ru/channel/abc/",
        ],
    )
    def test_rutube_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("rutube", url) is False
        assert sl.detect_platform(url) != "rutube"
