import pytest


class TestVelog:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://velog.io/@velopert", "https://velog.io/@velopert"),
        ],
    )
    def test_velog_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "velog"
        assert sl.is_valid("velog", url) is True
        assert sl.sanitize("velog", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://velog.io/@velopert/react-tutorial",
            "https://velog.io/trending",
        ],
    )
    def test_velog_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("velog", url) is False
        assert sl.detect_platform(url) != "velog"
