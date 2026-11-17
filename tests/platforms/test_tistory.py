"""Tests for Tistory platform."""
import pytest


class TestTistory:
    """Test Tistory platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://notice.tistory.com/2600",
            "https://www.tistory.com/",
        ],
    )
    def test_tistory_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("tistory", url) is False
        assert sl.detect_platform(url) != "tistory"
