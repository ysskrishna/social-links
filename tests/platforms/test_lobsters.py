import pytest


class TestLobsters:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://lobste.rs/u/jcs", "https://lobste.rs/~jcs"),
        ],
    )
    def test_lobsters_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "lobsters"
        assert sl.is_valid("lobsters", url) is True
        assert sl.sanitize("lobsters", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://lobste.rs/~jcs/stories",
            "https://lobste.rs/s/abc123/title",
        ],
    )
    def test_lobsters_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("lobsters", url) is False
        assert sl.detect_platform(url) != "lobsters"
