import pytest


class TestTrakt:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://trakt.tv/users/justin", "https://app.trakt.tv/profile/justin"),
        ],
    )
    def test_trakt_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "trakt"
        assert sl.is_valid("trakt", url) is True
        assert sl.sanitize("trakt", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://trakt.tv/shows/breaking-bad",
            "https://trakt.tv/users/justin/history",
        ],
    )
    def test_trakt_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("trakt", url) is False
        assert sl.detect_platform(url) != "trakt"
