import pytest


class TestZenn:
    @pytest.mark.parametrize(
        "url",
        [
            "https://zenn.dev/catnose/articles/abc",
        ],
    )
    def test_zenn_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("zenn", url) is False
        assert sl.detect_platform(url) != "zenn"
