"""Tests for OSF platform."""
import pytest


class TestOsf:
    """Test OSF platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://osf.io/abcde/files",
            "https://osf.io/preprints/",
        ],
    )
    def test_osf_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("osf", url) is False
        assert sl.detect_platform(url) != "osf"
