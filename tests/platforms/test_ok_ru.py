"""Tests for OK.ru platform."""
import pytest


class TestOkRu:
    """Test OK.ru platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://m.ok.ru/profile/561611456451", "https://ok.ru/profile/561611456451"),
        ],
    )
    def test_ok_ru_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "ok_ru"
        assert sl.is_valid("ok_ru", url) is True
        assert sl.sanitize("ok_ru", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://ok.ru/group/123",
            "https://ok.ru/profile/abc",
            "https://ok.ru/profile/561611456451/friends",
        ],
    )
    def test_ok_ru_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("ok_ru", url) is False
        assert sl.detect_platform(url) != "ok_ru"
