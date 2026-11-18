import pytest


class TestTopcoder:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.topcoder.com/members/tourist", "https://profiles.topcoder.com/tourist"),
        ],
    )
    def test_topcoder_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "topcoder"
        assert sl.is_valid("topcoder", url) is True
        assert sl.sanitize("topcoder", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://profiles.topcoder.com/tourist/stats",
            "https://www.topcoder.com/challenges",
        ],
    )
    def test_topcoder_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("topcoder", url) is False
        assert sl.detect_platform(url) != "topcoder"
