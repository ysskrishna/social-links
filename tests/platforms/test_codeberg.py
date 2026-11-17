"""Tests for Codeberg platform."""
import pytest


class TestCodeberg:
    """Test Codeberg platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://codeberg.org/forgejo/forgejo",
            "https://codeberg.org/explore",
            "https://codeberg.org/user",
        ],
    )
    def test_codeberg_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("codeberg", url) is False
        assert sl.detect_platform(url) != "codeberg"
