import pytest


class TestSlashdot:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://slashdot.org/~Bruce%20Perens", "https://slashdot.org/~Bruce%20Perens"),
        ],
    )
    def test_slashdot_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "slashdot"
        assert sl.is_valid("slashdot", url) is True
        assert sl.sanitize("slashdot", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://slashdot.org/story/24/01/01/123/title",
            "https://slashdot.org/~CmdrTaco/journal",
        ],
    )
    def test_slashdot_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("slashdot", url) is False
        assert sl.detect_platform(url) != "slashdot"
