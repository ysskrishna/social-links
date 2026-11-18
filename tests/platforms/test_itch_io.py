import pytest


class TestItchIo:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://leafo.itch.io/", "https://itch.io/profile/leafo"),
        ],
    )
    def test_itch_io_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "itch_io"
        assert sl.is_valid("itch_io", url) is True
        assert sl.sanitize("itch_io", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://leafo.itch.io/x-moon",
            "https://itch.io/games",
            "https://www.itch.io/",
        ],
    )
    def test_itch_io_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("itch_io", url) is False
        assert sl.detect_platform(url) != "itch_io"
