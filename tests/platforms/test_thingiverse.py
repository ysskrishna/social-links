import pytest


class TestThingiverse:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.thingiverse.com/MakerBot", "https://www.thingiverse.com/MakerBot"),
        ],
    )
    def test_thingiverse_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "thingiverse"
        assert sl.is_valid("thingiverse", url) is True
        assert sl.sanitize("thingiverse", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.thingiverse.com/thing:12345",
            "https://www.thingiverse.com/MakerBot/collections",
        ],
    )
    def test_thingiverse_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("thingiverse", url) is False
        assert sl.detect_platform(url) != "thingiverse"
