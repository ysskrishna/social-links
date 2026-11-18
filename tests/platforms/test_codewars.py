import pytest


class TestCodewars:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.codewars.com/kata/abc",
            "https://www.codewars.com/users/jhoffner/completed",
        ],
    )
    def test_codewars_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("codewars", url) is False
        assert sl.detect_platform(url) != "codewars"
