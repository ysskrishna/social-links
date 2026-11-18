import pytest


class TestAmeblo:
    @pytest.mark.parametrize(
        "url",
        [
            "https://ameblo.jp/ameba-official/entry-12345.html",
        ],
    )
    def test_ameblo_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("ameblo", url) is False
        assert sl.detect_platform(url) != "ameblo"
