"""Tests for ClawHub platform."""
import pytest


class TestClawhub:
    """Test ClawHub platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://clawhub.ai/steipete/skills/summarize",
        ],
    )
    def test_clawhub_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("clawhub", url) is False
        assert sl.detect_platform(url) != "clawhub"
