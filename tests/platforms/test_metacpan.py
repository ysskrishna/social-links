"""Tests for MetaCPAN platform."""
import pytest


class TestMetacpan:
    """Test MetaCPAN platform"""

    @pytest.mark.parametrize(
        "url",
        [
            "https://metacpan.org/pod/Moose",
            "https://metacpan.org/author/MIYAGAWA/releases",
            "https://metacpan.org/dist/Plack",
        ],
    )
    def test_metacpan_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("metacpan", url) is False
        assert sl.detect_platform(url) != "metacpan"
