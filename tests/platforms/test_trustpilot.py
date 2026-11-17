"""Tests for Trustpilot platform."""
import pytest


class TestTrustpilot:
    """Test Trustpilot platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://uk.trustpilot.com/users/5b4f2f0c4de5666d343f7c48", "https://www.trustpilot.com/users/5b4f2f0c4de5666d343f7c48"),
        ],
    )
    def test_trustpilot_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "trustpilot"
        assert sl.is_valid("trustpilot", url) is True
        assert sl.sanitize("trustpilot", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.trustpilot.com/review/amazon.com",
            "https://www.trustpilot.com/users/",
        ],
    )
    def test_trustpilot_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("trustpilot", url) is False
        assert sl.detect_platform(url) != "trustpilot"
