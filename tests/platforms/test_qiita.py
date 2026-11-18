import pytest


class TestQiita:
    @pytest.mark.parametrize(
        "url",
        [
            "https://qiita.com/jnchito/items/abc123",
        ],
    )
    def test_qiita_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("qiita", url) is False
        assert sl.detect_platform(url) != "qiita"
