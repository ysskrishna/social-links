import pytest


class TestAirbnb:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.airbnb.co.in/users/show/1", "https://www.airbnb.com/users/show/1"),
        ],
    )
    def test_airbnb_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "airbnb"
        assert sl.is_valid("airbnb", url) is True
        assert sl.sanitize("airbnb", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.airbnb.com/rooms/12345",
            "https://www.airbnb.com.evil.io/users/show/1",
            "https://www.airbnb.com/users/show/abc",
        ],
    )
    def test_airbnb_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("airbnb", url) is False
        assert sl.detect_platform(url) != "airbnb"
