"""Tests for Buy Me a Coffee platform."""
import pytest


class TestBuymeacoffee:
    """Test Buy Me a Coffee platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://buymeacoffee.com/ysskrishna/posts",
        ],
    )
    def test_buymeacoffee_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("buymeacoffee", url) is False
        assert sl.detect_platform(url) != "buymeacoffee"
