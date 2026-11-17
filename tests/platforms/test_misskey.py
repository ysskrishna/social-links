"""Tests for Misskey platform."""
import pytest


class TestMisskey:
    """Test Misskey platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://misskey.io/notes/9abc",
            "https://misskey.io/@syuilo/following",
            "https://misskey.io/syuilo",
        ],
    )
    def test_misskey_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("misskey", url) is False
        assert sl.detect_platform(url) != "misskey"
