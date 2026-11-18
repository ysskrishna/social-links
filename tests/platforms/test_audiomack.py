"""Tests for Audiomack platform."""
import pytest


class TestAudiomack:
    """Test Audiomack platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://audiomack.com/audiomack/song/some-song",
        ],
    )
    def test_audiomack_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("audiomack", url) is False
        assert sl.detect_platform(url) != "audiomack"
