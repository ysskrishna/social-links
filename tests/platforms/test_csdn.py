import pytest


class TestCsdn:
    @pytest.mark.parametrize(
        "url",
        [
            "https://blog.csdn.net/csdnnews/article/details/123",
            "https://blog.csdn.net/nav/ai",
        ],
    )
    def test_csdn_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("csdn", url) is False
        assert sl.detect_platform(url) != "csdn"
