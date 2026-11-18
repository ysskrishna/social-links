"""Tests for Are.na platform."""
import pytest


class TestAreNa:
    """Test Are.na platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.are.na/are-na-team/channel-slug",
            "https://www.are.na/block/123",
        ],
    )
    def test_are_na_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("are_na", url) is False
        assert sl.detect_platform(url) != "are_na"
