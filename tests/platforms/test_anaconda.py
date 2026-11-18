"""Tests for Anaconda.org platform."""
import pytest


class TestAnaconda:
    """Test Anaconda.org platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://anaconda.org/conda-forge/numpy",
        ],
    )
    def test_anaconda_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("anaconda", url) is False
        assert sl.detect_platform(url) != "anaconda"
