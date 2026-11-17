"""Tests for Qiita platform."""
import pytest


class TestQiita:
    """Test Qiita platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://qiita.com/jnchito/items/abc123",
            "https://qiita.com/tags",
            "https://qiita.com/trend",
            "https://qiita.com/settings",
        ],
    )
    def test_qiita_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("qiita", url) is False
        assert sl.detect_platform(url) != "qiita"
