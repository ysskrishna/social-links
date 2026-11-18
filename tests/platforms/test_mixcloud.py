import pytest


class TestMixcloud:
    @pytest.mark.parametrize(
        "url",
        [
            "https://www.mixcloud.com/NTSRadio/show-name-01-01-2024/",
        ],
    )
    def test_mixcloud_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("mixcloud", url) is False
        assert sl.detect_platform(url) != "mixcloud"
