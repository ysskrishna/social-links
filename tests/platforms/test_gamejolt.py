import pytest


class TestGamejolt:
    @pytest.mark.parametrize(
        "url",
        [
            "https://gamejolt.com/games/fnaf/123",
            "https://gamejolt.com/@CROS/games",
        ],
    )
    def test_gamejolt_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("gamejolt", url) is False
        assert sl.detect_platform(url) != "gamejolt"
