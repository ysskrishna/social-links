"""Tests for About.me platform."""
import pytest


class TestAboutMe:
    """Test About.me platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://about.me/tonyconrad/contact",
            "https://about.me/pricing",
            "https://about.me/login",
        ],
    )
    def test_about_me_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("about_me", url) is False
        assert sl.detect_platform(url) != "about_me"
