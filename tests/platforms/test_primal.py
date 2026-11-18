"""Tests for Primal platform."""
import pytest


class TestPrimal:
    """Test Primal platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://primal.net/p/82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2", "https://primal.net/p/82341f882b6eabcd2ba7f1ef90aad961cf074af15b9ef44a09f9d2a8fbfbe6a2"),
        ],
    )
    def test_primal_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "primal"
        assert sl.is_valid("primal", url) is True
        assert sl.sanitize("primal", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://primal.net/p/npub1short",
            "https://primal.net/e/note1abc",
            "https://primal.net/explore",
        ],
    )
    def test_primal_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("primal", url) is False
        assert sl.detect_platform(url) != "primal"
