"""Tests for start.gg platform."""
import pytest


class TestStartGg:
    """Test start.gg platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://smash.gg/user/0e1e3b6c", "https://www.start.gg/user/0e1e3b6c"),
        ],
    )
    def test_start_gg_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "start_gg"
        assert sl.is_valid("start_gg", url) is True
        assert sl.sanitize("start_gg", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.start.gg/tournament/genesis-9/details",
            "https://www.start.gg/user/0e1e3b6c/results",
        ],
    )
    def test_start_gg_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("start_gg", url) is False
        assert sl.detect_platform(url) != "start_gg"
