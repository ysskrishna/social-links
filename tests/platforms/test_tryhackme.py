"""Tests for TryHackMe platform."""
import pytest


class TestTryhackme:
    """Test TryHackMe platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://tryhackme.com/r/p/tryhackme", "https://tryhackme.com/p/tryhackme"),
        ],
    )
    def test_tryhackme_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "tryhackme"
        assert sl.is_valid("tryhackme", url) is True
        assert sl.sanitize("tryhackme", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://tryhackme.com/room/blue",
            "https://tryhackme.com/p/",
        ],
    )
    def test_tryhackme_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("tryhackme", url) is False
        assert sl.detect_platform(url) != "tryhackme"
