import pytest


class TestDiscogs:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.discogs.com/de/user/ysskrishna", "https://www.discogs.com/user/ysskrishna"),
        ],
    )
    def test_discogs_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "discogs"
        assert sl.is_valid("discogs", url) is True
        assert sl.sanitize("discogs", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.discogs.com/user/ysskrishna/collection",
            "https://www.discogs.com/artist/45-Aphex-Twin",
        ],
    )
    def test_discogs_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("discogs", url) is False
        assert sl.detect_platform(url) != "discogs"
