import pytest


class TestContra:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://contra.com/ysskrishna", "https://contra.com/ysskrishna"),
        ],
    )
    def test_contra_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "contra"
        assert sl.is_valid("contra", url) is True
        assert sl.sanitize("contra", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://contra.com/p/abc123-project",
            "https://contra.com/ysskrishna/services",
        ],
    )
    def test_contra_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("contra", url) is False
        assert sl.detect_platform(url) != "contra"
