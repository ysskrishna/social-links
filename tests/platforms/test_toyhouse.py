import pytest


class TestToyhouse:
    @pytest.mark.parametrize(
        "url",
        [
            "https://toyhou.se/~forums",
            "https://toyhou.se/123.character",
            "https://toyhou.se/Toyhouse/characters",
        ],
    )
    def test_toyhouse_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("toyhouse", url) is False
        assert sl.detect_platform(url) != "toyhouse"
