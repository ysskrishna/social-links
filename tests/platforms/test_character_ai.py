"""Tests for Character.AI platform."""
import pytest


class TestCharacterAi:
    """Test Character.AI platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://character.ai/chat/abc123",
            "https://character.ai/profile/",
        ],
    )
    def test_character_ai_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("character_ai", url) is False
        assert sl.detect_platform(url) != "character_ai"
