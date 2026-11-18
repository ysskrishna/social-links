import pytest


class TestXda:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://forum.xda-developers.com/m/ysskrishna.123456/", "https://xdaforums.com/m/ysskrishna.123456"),
        ],
    )
    def test_xda_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "xda"
        assert sl.is_valid("xda", url) is True
        assert sl.sanitize("xda", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://xdaforums.com/t/some-thread.123/",
            "https://xdaforums.com/m/ysskrishna/",
        ],
    )
    def test_xda_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("xda", url) is False
        assert sl.detect_platform(url) != "xda"
