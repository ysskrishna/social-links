"""Tests for Replicate platform."""
import pytest


class TestReplicate:
    """Test Replicate platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://replicate.com/stability-ai/sdxl",
        ],
    )
    def test_replicate_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("replicate", url) is False
        assert sl.detect_platform(url) != "replicate"
