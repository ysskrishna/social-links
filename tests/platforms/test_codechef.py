import pytest


class TestCodechef:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.codechef.com/problems/FLOW001",
            "https://www.codechef.com/users/",
        ],
    )
    def test_codechef_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("codechef", url) is False
        assert sl.detect_platform(url) != "codechef"
