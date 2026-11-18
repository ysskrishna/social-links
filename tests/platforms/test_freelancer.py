import pytest


class TestFreelancer:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://www.freelancer.in/u/ysskrishna", "https://www.freelancer.com/u/ysskrishna"),
        ],
    )
    def test_freelancer_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "freelancer"
        assert sl.is_valid("freelancer", url) is True
        assert sl.sanitize("freelancer", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://www.freelancer.com/projects/python/abc",
            "https://www.freelancer.com.evil.io/u/ysskrishna",
        ],
    )
    def test_freelancer_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("freelancer", url) is False
        assert sl.detect_platform(url) != "freelancer"
