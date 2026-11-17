"""Tests for Coursera platform."""
import pytest


class TestCoursera:
    """Test Coursera platform"""

    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.coursera.org/user/i/66b48af35b7a3e54fdf15aff3da8a918", "https://www.coursera.org/user/66b48af35b7a3e54fdf15aff3da8a918"),
        ],
    )
    def test_coursera_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "coursera"
        assert sl.is_valid("coursera", url) is True
        assert sl.sanitize("coursera", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.coursera.org/learn/machine-learning",
            "https://www.coursera.org/user/ysskrishna",
            "https://www.coursera.org/user/85dca6cc1c1ccacdb8d6cbc3853c8eff/accomplishments",
        ],
    )
    def test_coursera_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("coursera", url) is False
        assert sl.detect_platform(url) != "coursera"
