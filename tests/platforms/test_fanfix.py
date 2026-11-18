import pytest


class TestFanfix:
    @pytest.mark.parametrize(
        "url",
        [
            "https://app.fanfix.io/discover",
            "https://app.fanfix.io/@ysskrishna/post/1",
        ],
    )
    def test_fanfix_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("fanfix", url) is False
        assert sl.detect_platform(url) != "fanfix"
