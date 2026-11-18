import pytest


class TestThrone:
    @pytest.mark.parametrize(
        "url",
        [
            "https://throne.com/ysskrishna/item/123",
        ],
    )
    def test_throne_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("throne", url) is False
        assert sl.detect_platform(url) != "throne"
