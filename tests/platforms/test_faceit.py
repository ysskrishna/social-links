import pytest


class TestFaceit:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.faceit.com/players/s1mple", "https://www.faceit.com/en/players/s1mple"),
            ("https://www.faceit.com/en/players/s1mple/stats/cs2", "https://www.faceit.com/en/players/s1mple"),
        ],
    )
    def test_faceit_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "faceit"
        assert sl.is_valid("faceit", url) is True
        assert sl.sanitize("faceit", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.faceit.com/en/cs2/room/1-abc",
            "https://www.faceit.com/en/players/",
        ],
    )
    def test_faceit_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("faceit", url) is False
        assert sl.detect_platform(url) != "faceit"
