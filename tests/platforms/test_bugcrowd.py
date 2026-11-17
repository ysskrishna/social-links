"""Tests for Bugcrowd platform."""
import pytest


class TestBugcrowd:
    """Test Bugcrowd platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://bugcrowd.com/engagements/tesla",
            "https://bugcrowd.com/h/nahamsec/kudos",
        ],
    )
    def test_bugcrowd_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("bugcrowd", url) is False
        assert sl.detect_platform(url) != "bugcrowd"
