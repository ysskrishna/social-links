import pytest


class TestHackerone:
    @pytest.mark.parametrize(
        "url",
        [
            "https://hackerone.com/reports/123456",
            "https://hackerone.com/nahamsec/badges",
        ],
    )
    def test_hackerone_rejects_non_profile_urls(self, sl, url):
        assert sl.is_valid("hackerone", url) is False
        assert sl.detect_platform(url) != "hackerone"
