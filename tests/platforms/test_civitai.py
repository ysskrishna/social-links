"""Tests for Civitai platform."""
import pytest


class TestCivitai:
    """Test Civitai platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://civitai.com/models/4201/realistic-vision",
            "https://civitai.com/user/ysskrishna/models",
        ],
    )
    def test_civitai_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("civitai", url) is False
        assert sl.detect_platform(url) != "civitai"
