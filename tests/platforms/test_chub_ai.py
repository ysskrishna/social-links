"""Tests for Chub.ai platform."""
import pytest


class TestChubAi:
    """Test Chub.ai platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://chub.ai/characters/abc/def",
            "https://chub.ai/users/ysskrishna/lorebooks",
        ],
    )
    def test_chub_ai_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("chub_ai", url) is False
        assert sl.detect_platform(url) != "chub_ai"
