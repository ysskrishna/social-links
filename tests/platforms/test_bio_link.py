"""Tests for Bio.link platform."""
import pytest


class TestBioLink:
    """Test Bio.link platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://bio.link/ysskrishna/abc",
        ],
    )
    def test_bio_link_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("bio_link", url) is False
        assert sl.detect_platform(url) != "bio_link"
