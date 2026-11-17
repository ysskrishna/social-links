"""Tests for Depop platform."""
import pytest


class TestDepop:
    """Test Depop platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.depop.com/products/abc-123/",
            "https://www.depop.com/ysskrishna/likes",
        ],
    )
    def test_depop_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("depop", url) is False
        assert sl.detect_platform(url) != "depop"
