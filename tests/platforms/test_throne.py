"""Tests for Throne platform."""
import pytest


class TestThrone:
    """Test Throne platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://throne.com/ysskrishna/item/123",
            "https://throne.com/creators",
        ],
    )
    def test_throne_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("throne", url) is False
        assert sl.detect_platform(url) != "throne"
