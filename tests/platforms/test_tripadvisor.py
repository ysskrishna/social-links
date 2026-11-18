import pytest


class TestTripadvisor:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.tripadvisor.co.uk/Profile/ysskrishna", "https://www.tripadvisor.com/Profile/ysskrishna"),
        ],
    )
    def test_tripadvisor_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "tripadvisor"
        assert sl.is_valid("tripadvisor", url) is True
        assert sl.sanitize("tripadvisor", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.tripadvisor.com/Hotel_Review-g1-d2.html",
            "https://www.tripadvisor.com.evil.io/Profile/ysskrishna",
        ],
    )
    def test_tripadvisor_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("tripadvisor", url) is False
        assert sl.detect_platform(url) != "tripadvisor"
