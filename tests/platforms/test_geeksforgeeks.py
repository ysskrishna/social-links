"""Tests for GeeksforGeeks platform."""
import pytest


class TestGeeksforgeeks:
    """Test GeeksforGeeks platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.geeksforgeeks.org/profile/sandeepjainlinkedin", "https://www.geeksforgeeks.org/profile/sandeepjainlinkedin"),
        ],
    )
    def test_geeksforgeeks_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "geeksforgeeks"
        assert sl.is_valid("geeksforgeeks", url) is True
        assert sl.sanitize("geeksforgeeks", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.geeksforgeeks.org/python-programming-language/",
            "https://www.geeksforgeeks.org/user/sandeepjainlinkedin/articles",
        ],
    )
    def test_geeksforgeeks_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("geeksforgeeks", url) is False
        assert sl.detect_platform(url) != "geeksforgeeks"
