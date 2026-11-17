"""Tests for SOOP (AfreecaTV) platform."""
import pytest


class TestSoop:
    """Test SOOP (AfreecaTV) platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://ch.sooplive.co.kr/phonics1", "https://www.sooplive.com/station/phonics1"),
            ("https://bj.afreecatv.com/phonics1", "https://www.sooplive.com/station/phonics1"),
        ],
    )
    def test_soop_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "soop"
        assert sl.is_valid("soop", url) is True
        assert sl.sanitize("soop", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.sooplive.com/station/phonics1/post/123",
            "https://play.sooplive.co.kr/phonics1/123",
        ],
    )
    def test_soop_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("soop", url) is False
        assert sl.detect_platform(url) != "soop"
