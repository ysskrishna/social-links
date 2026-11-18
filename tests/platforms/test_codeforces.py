import pytest


class TestCodeforces:
    @pytest.mark.parametrize(
        "url,sanitized",
        [
            ("https://codeforces.com/profile/tourist?locale=ru", "https://codeforces.com/profile/tourist"),
            ("https://m1.codeforces.com/profile/tourist", "https://codeforces.com/profile/tourist"),
        ],
    )
    def test_codeforces_url_variants(self, sl, url, sanitized):
        assert sl.detect_platform(url) == "codeforces"
        assert sl.is_valid("codeforces", url) is True
        assert sl.sanitize("codeforces", url) == sanitized

    @pytest.mark.parametrize(
        "url",
        [
            "https://codeforces.com/contest/1/problem/A",
            "https://codeforces.com/profile/tourist/blog",
        ],
    )
    def test_codeforces_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("codeforces", url) is False
        assert sl.detect_platform(url) != "codeforces"
