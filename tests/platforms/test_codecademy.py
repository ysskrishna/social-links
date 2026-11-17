"""Tests for Codecademy platform."""
import pytest


class TestCodecademy:
    """Test Codecademy platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.codecademy.com/learn/learn-python-3",
            "https://www.codecademy.com/profiles/",
        ],
    )
    def test_codecademy_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("codecademy", url) is False
        assert sl.detect_platform(url) != "codecademy"
