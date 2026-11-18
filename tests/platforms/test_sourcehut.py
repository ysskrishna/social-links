"""Tests for SourceHut platform."""
import pytest


class TestSourcehut:
    """Test SourceHut platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://git.sr.ht/~sircmpwn/", "https://sr.ht/~sircmpwn"),
            ("https://todo.sr.ht/~sircmpwn", "https://sr.ht/~sircmpwn"),
        ],
    )
    def test_sourcehut_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "sourcehut"
        assert sl.is_valid("sourcehut", url) is True
        assert sl.sanitize("sourcehut", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://git.sr.ht/~sircmpwn/hare",
            "https://sr.ht/~sircmpwn/hare/",
            "https://evilsr.ht/~sircmpwn",
        ],
    )
    def test_sourcehut_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("sourcehut", url) is False
        assert sl.detect_platform(url) != "sourcehut"
